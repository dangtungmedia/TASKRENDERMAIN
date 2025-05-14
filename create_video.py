from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.fx.all import fadein, fadeout, resize
from moviepy.video.fx.zoom_in import zoom_in

# Hiển thị version đang dùng (debug)
import moviepy
print("MoviePy version:", moviepy.__version__)

# Đường dẫn ảnh
image_path = "dong_co_thanhnien_PXRW.jpg"

# Thời lượng video
duration = 10  # giây

# Tạo clip từ ảnh, thêm hiệu ứng
clip = (
    ImageClip(image_path)
    .set_duration(duration)
    .fx(resize, width=1280)
    .fx(fadein, 1)
    .fx(fadeout, 1)
    .fx(zoom_in, 1.1)
)

# Ghi ra video
clip.write_videofile("output.mp4", fps=30)
