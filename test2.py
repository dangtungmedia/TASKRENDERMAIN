import subprocess


def loop_video_with_audio(input_video: str, input_audio: str, output_file: str, preset: str = 'p1', cq: int = 28):
    """
    Lặp video vô hạn để tạo video dài bằng đúng audio, encode video hevc_nvenc, copy audio gốc.
    - input_video: file video đầu vào để lặp
    - input_audio: file audio đầu vào
    - output_file: file đầu ra
    - preset: preset ffmpeg nvenc, mặc định 'p1'
    - cq: chất lượng constant quality, mặc định 28
    """
    cmd = [
        'ffmpeg',
        '-stream_loop', '-1',
        '-i', input_video,
        '-i', input_audio,
        '-shortest',
        '-map', '0:v:0',
        '-map', '1:a:0',
        '-c:v', 'hevc_nvenc',
        '-preset', preset,
        '-cq', str(cq),
        '-c:a', 'copy',
        '-movflags', '+faststart',
        output_file
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"Video đã được tạo thành công: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi tạo video: {e}")

video_out_h265 = "media/86747/output_h265.mp4"
output_path_audio ="media/86747/audio.wav"
out_video ="test.mp4"

loop_video_with_audio(video_out_h265,output_path_audio,out_video, preset='p1', cq=28)
    