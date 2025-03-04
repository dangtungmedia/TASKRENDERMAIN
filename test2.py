import yt_dlp as youtube_dl

# URL của video YouTube
url = "https://www.youtube.com/watch?v=mh9Wlt7r_fw"  # Thay bằng URL video của bạn

# Cấu hình để lấy thông tin video
ydl_opts = {
    'quiet': True,  # Ẩn thông báo không cần thiết
    'force_generic_extractor': True,  # Sử dụng extractor tổng quát
}

# Sử dụng yt-dlp để lấy thông tin video
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)

    # Lấy số lượt xem và lượt thích
    views = info_dict.get('view_count', None)
    likes = info_dict.get('like_count', None)

    # Kiểm tra thông tin kênh có hợp lệ và lấy số người đăng ký kênh
    channel_info = info_dict.get('channel', {})
    subscribers = None
    if isinstance(channel_info, dict):
        subscribers = channel_info.get('subscriber_count', None)

# In ra thông tin
if views is not None:
    print(f"Số lượt xem: {views}")
else:
    print("Không thể lấy số lượt xem.")

if likes is not None:
    print(f"Số lượt thích: {likes}")
else:
    print("Không thể lấy số lượt thích.")
