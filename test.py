import os
import re
import time
from urllib import request
from urllib.error import URLError, HTTPError

def get_youtube_thumbnail(youtube_url, video_id):
    try:
        video_id = str(video_id)

        pattern = r'(?:https?:\/\/)?(?:www\.)?youtu(?:be)?\.(?:com|be)(?:\/watch\?v=|\/)([^\s&]+)'
        match = re.findall(pattern, youtube_url)

        if not match:
            print("❌ Invalid YouTube URL")
            return False

        video_id_youtube = match[0]

        thumbnails = {
            'max': f'https://i3.ytimg.com/vi/{video_id_youtube}/maxresdefault.jpg',
            'hq': f'https://i3.ytimg.com/vi/{video_id_youtube}/hqdefault.jpg',
            'mq': f'https://i3.ytimg.com/vi/{video_id_youtube}/mqdefault.jpg',
            'sd': f'https://i3.ytimg.com/vi/{video_id_youtube}/sddefault.jpg',
            'default': f'https://i3.ytimg.com/vi/{video_id_youtube}/default.jpg'
        }

        save_dir = os.path.join('media', video_id, 'thumbnail')
        os.makedirs(save_dir, exist_ok=True)

        for quality, url in thumbnails.items():
            try:
                response = request.urlopen(url)
                if response.status == 200:
                    file_path = os.path.join(save_dir, f"{video_id_youtube}_{quality}.jpg")
                    with open(file_path, 'wb') as f:
                        f.write(response.read())
                    print(f"✅ Tải thành công: {file_path}")
                    return file_path
            except (HTTPError, URLError) as e:
                print(f"❌ Lỗi khi tải ảnh {quality}: {e}")
                time.sleep(1)
                continue

        print("❌ Không tìm thấy ảnh nào tải được")
        return False

    except Exception as e:
        print(f"❌ Lỗi không xác định: {e}")
        return False

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=xYtNiVIh3PU"
    video_id = "xYtNiVIh3PU"
    get_youtube_thumbnail(youtube_url, video_id)
