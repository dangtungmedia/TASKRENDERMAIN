from pytube import YouTube

# URL video YouTube
video_url = 'https://www.youtube.com/watch?v=aKEatGCJUGM'  # Thay VIDEO_ID bằng ID thật

# Tải đối tượng YouTube
yt = YouTube(video_url)

# Kiểm tra phụ đề có sẵn
print("Các phụ đề có sẵn:")
print(yt.captions)

# Lấy phụ đề tiếng Anh (nếu có)
caption = yt.captions.get_by_language_code('en')

if caption:
    # Lưu phụ đề dạng .srt (SubRip)
    srt_captions = caption.generate_srt_captions()
    with open("subtitle_en.srt", "w", encoding="utf-8") as f:
        f.write(srt_captions)
    print("Đã lưu phụ đề vào 'subtitle_en.srt'")
else:
    print("Không tìm thấy phụ đề tiếng Anh.")
