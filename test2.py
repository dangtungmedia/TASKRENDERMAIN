import subprocess
import os
import re

# === Cấu hình ===
VIDEO_PATH = "zs5xw1B.mp4"
AUDIO_PATH = "temp_audio.wav"
MIN_SILENCE_LEN = 1.0  # im lặng ít nhất 1 giây
SILENCE_THRESH = -40   # ngưỡng âm lượng (dB)
AD_SPACING_SECONDS = 120
MAX_AD_DURATION = 180

# === Bước 1: Tách audio từ video ===
def extract_audio(video_path, audio_path):
    command = [
        "ffmpeg", "-y", "-i", video_path,
        "-vn", "-acodec", "pcm_s16le",
        "-ar", "44100", "-ac", "2", audio_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# === Bước 2: Dùng ffmpeg để detect khoảng im lặng ===
def detect_silences(audio_path):
    command = [
        "ffmpeg", "-i", audio_path,
        "-af", f"silencedetect=noise={SILENCE_THRESH}dB:d={MIN_SILENCE_LEN}",
        "-f", "null", "-"
    ]
    result = subprocess.run(command, stderr=subprocess.PIPE, text=True)
    output = result.stderr

    silence_times = []
    current_start = None
    for line in output.splitlines():
        if "silence_start" in line:
            current_start = float(re.search(r"silence_start: (\d+\.?\d*)", line).group(1))
        elif "silence_end" in line and current_start is not None:
            end = float(re.search(r"silence_end: (\d+\.?\d*)", line).group(1))
            silence_times.append((current_start, end))
            current_start = None
    return silence_times

# === Bước 3: Lấy thời lượng video bằng ffprobe ===
def get_video_duration(video_path):
    command = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        video_path
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return float(result.stdout.strip())

# === Bước 4: Chọn thời điểm chèn quảng cáo ===
def get_ad_insert_points(silences, video_duration):
    insert_points = []
    current_time = 0

    for silence_start, _ in silences:
        if silence_start >= current_time + AD_SPACING_SECONDS:
            insert_points.append(silence_start)
            current_time = silence_start
        if silence_start > video_duration - MAX_AD_DURATION:
            break

    return insert_points

# === Main ===
def main():
    print("▶ Tách audio từ video...")
    extract_audio(VIDEO_PATH, AUDIO_PATH)

    print("🔎 Tìm đoạn im lặng...")
    silences = detect_silences(AUDIO_PATH)

    print("⏱ Lấy độ dài video...")
    duration = get_video_duration(VIDEO_PATH)

    print("📌 Tính điểm chèn quảng cáo...")
    ad_times = get_ad_insert_points(silences, duration)

    for i, t in enumerate(ad_times, 1):
        print(f"📍 Quảng cáo {i}: chèn tại giây {round(t, 2)}")

    if os.path.exists(AUDIO_PATH):
        os.remove(AUDIO_PATH)

if __name__ == "__main__":
    main()
