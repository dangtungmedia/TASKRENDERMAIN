import os
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# 👉 Scope này đủ để tạo file/thư mục và truy cập file


def authenticate():
    """Xác thực với Google Drive API và lấy credentials"""
    creds = None
    SCOPES = ["https://www.googleapis.com/auth/drive"]
    # Kiểm tra file token.json để lấy thông tin xác thực
    if os.path.exists("token.json"):
        try:
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        except:
            return None
    # Nếu không có creds hợp lệ, thực hiện xác thực
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
            # Lưu credentials để dùng lại
            with open("token.json", "w") as token:
                token.write(creds.to_json())
    
    return creds


def create_subfolder(parent_folder_id, subfolder_name):
    """Tạo thư mục con trong Google Drive"""
    try:
        creds = authenticate()
        if not creds:
            return 
        service = build("drive", "v3", credentials=creds)

        # Định nghĩa metadata cho thư mục con
        folder_metadata = {
            "name": subfolder_name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [parent_folder_id]
        }

        # Tạo thư mục con
        folder = service.files().create(body=folder_metadata, fields="id").execute()

        print(f"✅ Thư mục '{subfolder_name}' đã được tạo với ID: {folder.get('id')}")
        return folder.get('id')
    
    except HttpError as error:
        print(f"❌ Lỗi xảy ra: {error}")
        return None

def upload_file(file_path, folder_id):
    """Tải file lên Google Drive và lấy URL chia sẻ"""
    try:
        creds = authenticate()
        if not creds:
            return 
        service = build("drive", "v3", credentials=creds)

        # Định nghĩa metadata cho file
        file_metadata = {
            "name": os.path.basename(file_path),
            "parents": [folder_id]
        }

        # Tạo đối tượng MediaFileUpload và chỉ định callback
        media = MediaFileUpload(file_path, mimetype="application/octet-stream", chunksize=1024*1024, resumable=True)

        # Upload file với callback
        request = service.files().create(body=file_metadata, media_body=media, fields="id, webViewLink")
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"Tải lên: {status.progress() * 100:.2f}%")

        # Lấy ID và link chia sẻ
        file_id = response.get("id")
        web_view_link = response.get("webViewLink")
        
        print(f"✅ File '{file_path}' đã được tải lên thành công với ID: {file_id}")
        print(f"🔗 Đường dẫn chia sẻ: {web_view_link}")

        # Cập nhật quyền truy cập để chia sẻ file
        update_permissions(service, file_id)

        return file_id, web_view_link

    except HttpError as error:
        print(f"❌ Lỗi xảy ra khi tải lên file: {error}")
        return None, None

def update_permissions(service, file_id):
    """Cập nhật quyền chia sẻ cho file để bất kỳ ai có link có thể xem"""
    try:
        # Tạo quyền cho người dùng "anyone" có thể xem file
        permissions = {
            'type': 'anyone',
            'role': 'reader',  # Quyền đọc
        }
        # Tạo quyền truy cập chia sẻ cho file
        service.permissions().create(
            fileId=file_id,
            body=permissions
        ).execute()
        print(f"✅ Đã cập nhật quyền chia sẻ cho file {file_id}. File có thể được truy cập công khai.")
    except HttpError as error:
        print(f"❌ Lỗi xảy ra khi cập nhật quyền: {error}")

def delete_file(file_id):
    """Xoá file vĩnh viễn khỏi Google Drive"""
    creds = authenticate()
    if not creds:
        return 
    service = build("drive", "v3", credentials=creds)
    try:
        # Xóa file vĩnh viễn (không chuyển vào thùng rác)
        service.files().delete(fileId=file_id).execute()
        print(f"✅ Đã xóa file {file_id} vĩnh viễn khỏi Google Drive.")
    except HttpError as error:
        print(f"❌ Lỗi xảy ra khi xóa file: {error}")

def check_file_exists(file_id):
    """Kiểm tra xem file có tồn tại trên Google Drive không"""
    creds = authenticate()
    if not creds:
        return 
    service = build("drive", "v3", credentials=creds)
    try:
        file = service.files().get(fileId=file_id).execute()
        print(f"File tồn tại: {file['name']}")
        return True
    except HttpError as error:
        if error.resp.status == 404:
            print(f"❌ File không tìm thấy với ID: {file_id}")
            return False
        else:
            print(f"❌ Lỗi: {error}")
            return False

def download_file(file_id):
    """Tải file từ Google Drive về máy tính"""
    creds = authenticate()
    if not creds:
        return 
    service = build("drive", "v3", credentials=creds)
    
    try:
        # Lấy thông tin file từ ID để lấy tên file
        file = service.files().get(fileId=file_id).execute()
        file_name = file["name"]  # Lấy tên file từ thông tin file

        # Tạo đường dẫn lưu file (nếu không có thư mục sẽ tạo mới)
        destination_path = os.path.join(os.getcwd(), file_name)

        # Lấy nội dung file từ Google Drive
        request = service.files().get_media(fileId=file_id)

        # Mở file đích để ghi nội dung tải về
        with open(destination_path, "wb") as file:
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(f"Tải xuống: {status.progress() * 100:.2f}%")
        
        print(f"✅ File đã được tải xuống thành công: {destination_path}")
    
    except Exception as error:
        print(f"❌ Lỗi khi tải file: {error}")

def convert_size(size_in_bytes):
    """Chuyển đổi dung lượng từ byte sang GB hoặc TB"""
    if size_in_bytes >= 1024**4:  # Nếu dung lượng >= 1 TB
        return f"{size_in_bytes / (1024 ** 4):.2f} TB"
    else:  # Nếu dung lượng nhỏ hơn 1 TB, dùng GB
        return f"{size_in_bytes / (1024 ** 3):.2f} GB"

def check_drive_storage():
    creds = authenticate()
    if not creds:
        return 
    service = build('drive', 'v3', credentials=creds)
    # Lấy thông tin về dung lượng Drive
    about_info = service.about().get(fields="storageQuota").execute()

    # Dung lượng đã sử dụng và dung lượng tổng
    used_space = int(about_info['storageQuota']['usage'])
    total_space = int(about_info['storageQuota']['limit'])

    # Tính tỷ lệ phần trăm dung lượng đã sử dụng
    usage_percentage = (used_space / total_space) * 100

    stronger_data = {
        "total": f"{total_space / (1024 ** 4):.2f} TB",
        "used" :convert_size(used_space),
        "percent_used":usage_percentage
    }
    return stronger_data

# if __name__ == "__main__":
#     subfolder_id = "1apzRBnKoOMKRPFq4dEu0DuYkaxQTxVGY"  # ID thư mục cha
#     # subfolder_name = "test_thu_muc_2"
#     # # Tạo thư mục con
#     # subfolder_id = create_subfolder(parent_folder_id, subfolder_name)

#     if subfolder_id:
#         # Đường dẫn tới file cần tải lên
#         file_path = "media2.mp4"  # Thay thế bằng đường dẫn file của bạn
        
#         # Ghi lại thời gian bắt đầu tải lên
#         start_time = time.time()
        
#         # Tải file lên thư mục con vừa tạo và lấy đường dẫn chia sẻ
#         file_id, web_view_link = upload_file(file_path, subfolder_id)
        
#         # Ghi lại thời gian kết thúc tải lên
#         end_time = time.time()
        
#         # Tính toán thời gian tải xong
#         elapsed_time = end_time - start_time
        
#         # Hiển thị thời gian tải xong
#         print(f"Video tải lên thành công. Thời gian tải: {elapsed_time:.2f} giây")
#         print(web_view_link)


#     # file_id = "14NlhBsJwtyRMWMFqhMz8qRqtjaJYNV2K"
#     # if check_file_exists(file_id):
#     #     delete_file(file_id)

#     # file_id = "14NlhBsJwtyRMWMFqhMz8qRqtjaJYNV2K"  # ID của file trên Google Drive    
#     # # Tải file về máy
#     # download_file(file_id)

#     check_drive_storage()