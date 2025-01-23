import os
import hashlib

def calculate_file_hash(file_path):
    """
    Tính hash của tệp để so sánh nội dung.
    """
    hash_md5 = hashlib.md5()  # Sử dụng MD5 để tính hash
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def remove_duplicates_in_directory(directory):
    """
    Xóa các tệp trùng lặp trong thư mục và in số lượng tệp bị xóa.
    """
    seen_hashes = {}
    duplicate_count = 0

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)

            if file_hash in seen_hashes:
                # Nếu hash đã tồn tại, xóa tệp trùng lặp
                print(f"Xóa tệp trùng lặp: {file_path}")
                os.remove(file_path)
                duplicate_count += 1
            else:
                # Nếu hash chưa tồn tại, lưu lại
                seen_hashes[file_hash] = file_path

    print(f"Tổng số tệp trùng lặp đã bị xóa: {duplicate_count}")

# Thư mục cần xử lý
directory_path = "video"  # Thay bằng đường dẫn thư mục của bạn
remove_duplicates_in_directory(directory_path)
