import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
from fake_useragent import UserAgent

# Tắt cảnh báo SSL nếu cần
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def send_typecast_request():
    url = "https://typecast.ai/api/speak/batch/post"
    ua = UserAgent()
    # Sử dụng CHÍNH XÁC headers từ Postman
    headers = {
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1NzA4MWNhOWNiYjM3YzIzNDk4ZGQzOTQzYmYzNzFhMDU4ODNkMjgiLCJ0eXAiOiJKV1QifQ.eyJfaWQiOiI2N2U2Njg3MGQ3NDQ3ZWZlMmVmYTBiNjkiLCJhcHByb3ZlZCI6dHJ1ZSwiYXV0aHR5cGUiOiJmaXJlYmFzZSIsInByb3ZpZGVyIjoicGFzc3dvcmQiLCJpc19wYWlkIjpmYWxzZSwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3R5cGVjYXN0LXByb2QtNTBjYjEiLCJhdWQiOiJ0eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXV0aF90aW1lIjoxNzQ1MjI0OTYxLCJ1c2VyX2lkIjoidUVOZjVsOXZqNVl6TWs3djZjOUJzTmIyNTZBMyIsInN1YiI6InVFTmY1bDl2ajVZek1rN3Y2YzlCc05iMjU2QTMiLCJpYXQiOjE3NDUyMjQ5NjEsImV4cCI6MTc0NTIyODU2MSwiZW1haWwiOiJzaGs1MzAxNEBqaW9zby5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzaGs1MzAxNEBqaW9zby5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJjdXN0b20ifX0.dYTzd1PrqBIm4zCz8AslLmue8oIOT042ByoU9OzbrecGIJT97baxuX2GbtsOyf_-GH-DFoMAM4UqoDzHeCpo09DKgIVrE36sCuD36SQWJwVfE1Nrv3LFry0rxI5lXCDO5B4Ru0ZHWVeBlXDIzmFbziTvH8YBAgUQdiSutbPertOw33KdGTb10Zmm22SYyw4cw7oV3l6SLER-8iyLikuFk7OAkMQ1KZep7lyX8XLkHPYmCkopOuOynQ7Fl-HzAXZBGWjFxIhc4Fc_KEb5Qc6vPDMGf6aRe7G-yVj7CjfVE4d6A9I9BtQhcS7jbo4fYO9mlcIUGotuONWyAt35z-fx4Q",
        "Content-Type": "application/json",
        "User-Agent": ua.google
    }

    # Sử dụng CHÍNH XÁC payload từ cURL
    payload_str = '''[
  {
    "text": "hello my nam is tung 1  2 3  4  5  6  7  8  9 10 ",
    "actor_id": "600697fd8a8ea9b977284703",
    "tempo": 1,
    "pitch": 0,
    "style_label": "normal-1",
    "style_label_version": "v5",
    "emotion_scale": 1,
    "lang": "auto",
    "mode": "one-vocoder",
    "retake": true,
    "bp_c_l": true,
    "adjust_lastword": 0
  }
]'''

    print("URL:", url)
    print("Headers:", json.dumps(headers, indent=2))
    print("Payload:", payload_str)

    try:
        # Thử nhiều cách gửi request
        print("\n--- Phương pháp 1: Gửi payload dạng string ---")
        response1 = requests.post(url, headers=headers, data=payload_str, verify=False)
        print(f"Status code: {response1.status_code}")
        print(f"Response: {response1.text}")

        print("\n--- Phương pháp 2: Gửi payload dạng JSON ---")
        payload_json = json.loads(payload_str)
        response2 = requests.post(url, headers=headers, json=payload_json, verify=False)
        print(f"Status code: {response2.status_code}")
        print(f"Response: {response2.text}")

        return response1 if response1.status_code == 200 else response2

    except Exception as e:
        print(f"Lỗi: {str(e)}")
        return None

if __name__ == "__main__":
    send_typecast_request()