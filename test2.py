import json
import subprocess
import os


def get_video_duration(video_path):
    # Lệnh ffprobe để lấy thông tin video dưới dạng JSON
    command = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=duration",
        "-of", "json",
        video_path
    ]
    
    # Chạy lệnh ffprobe và lấy đầu ra
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Nếu có lỗi khi chạy lệnh, trả về None (để xử lý video lỗi)
    if result.returncode != 0:
        return None
    
    # Chuyển đổi đầu ra từ JSON thành dictionary
    result_json = json.loads(result.stdout)
    
    # Lấy thời lượng từ dictionary
    duration = float(result_json['streams'][0]['duration'])
    
    return duration

def process_videos(path):
    # Khởi tạo biến đếm số lượng video
    valid_videos = 0
    invalid_videos = 0
    
    # Duyệt qua tất cả các tệp trong thư mục
    for filename in os.listdir(path):
        video_path = os.path.join(path, filename)
        
        # Kiểm tra xem tệp có phải là video (có thể mở rộng thêm các đuôi khác nếu cần)
        if os.path.isfile(video_path) and filename.endswith(('.mp4', '.mkv', '.avi')):
            # Gọi hàm get_video_duration để kiểm tra video có hợp lệ không
            duration = get_video_duration(video_path)
            
            if duration is not None:
                print(f"Video {filename} hợp lệ, thời lượng: {duration} giây")
                valid_videos += 1
            else:
                print(f"Video {filename} bị lỗi, sẽ xóa...")
                os.remove(video_path)  # Xóa video lỗi
                invalid_videos += 1

    print(f"\nSố lượng video hợp lệ: {valid_videos}")
    print(f"Số lượng video bị lỗi và đã xóa: {invalid_videos}")

# Thư mục chứa video
video_directory = "video"

# Xử lý các video trong thư mục
process_videos(video_directory)
