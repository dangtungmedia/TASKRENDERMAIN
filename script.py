import time
import aiohttp
import asyncio
import json
from fake_useragent import UserAgent
import requests
print("test")

def send_typecast_request():
    url = "https://typecast.ai/api/speak/batch/post"
    ua = UserAgent()

    headers = {
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjY3ZDhjZWU0ZTYwYmYwMzYxNmM1ODg4NTJiMjA5MTZkNjRjMzRmYmEiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVHVuZyBkYW5nIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FHTm15eGIzZWg4cjAzYmNqRkxkT3ZIcFpNeDZPOWR3TVdFYWk3X18tWXdLPXM5Ni1jIiwiX2lkIjoiNjQ1NTQ0ZDFiYzI5M2FhYjQzZmZhMWE2IiwiYXBwcm92ZWQiOnRydWUsImF1dGh0eXBlIjoiZmlyZWJhc2UiLCJwcm92aWRlciI6InBhc3N3b3JkIiwiaXNfcGFpZCI6ZmFsc2UsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS90eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXVkIjoidHlwZWNhc3QtcHJvZC01MGNiMSIsImF1dGhfdGltZSI6MTc0NzIyMTc1OSwidXNlcl9pZCI6Ikc1RjhwdHFiT2VUQnlOMVdDeXRyamp0ZVhkZDIiLCJzdWIiOiJHNUY4cHRxYk9lVEJ5TjFXQ3l0cmpqdGVYZGQyIiwiaWF0IjoxNzQ3MjIxNzU5LCJleHAiOjE3NDcyMjUzNTksImVtYWlsIjoiZGFuZ3R1bmdtZWRpYUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJkYW5ndHVuZ21lZGlhQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6ImN1c3RvbSJ9fQ.dBhD19_3xdqKfY4t3JC1qwD7Rl7ma3F-8tAWgYmkl64DfIniKW61yEqwfBcBvn4pBj-3LsZc4SDjAnLGrO9gZOeNyfSEOwTO0FUZvR9_4T5v3Cyafq4ayqpB6Nkgfao_4McbrklSgPgte4S8z51psly_8B6XB08BNxC2aC2NzIuFMkuGUiDJrHhFVyTrCJ8V6vNo4S-SN7yVKPYapPZREjSHBmstcWNf5WObcGtiOcznO83xOI_43aZfBCQPi1sz5VRlHoyBgkPl-ibvDBNCyayNa-GHtzQbtJjdvSqd5Dae6SRj2rIa_Hhz3ZDK5ds6eJx_hHs3Vp0gG9iAj53gQw",  # (token rút gọn)
        "Content-Type": "application/json",
        "User-Agent": ua.google
    }

    payload = [
        {
            "text": "hello my name is tung 1 2 3 4 5 6 7 8 9 10",
            "actor_id": "600697fd8a8ea9b977284703",
            "tempo": 1,
            "pitch": 0,
            "style_label": "normal-1",
            "style_label_version": "v5",
            "emotion_scale": 1,
            "lang": "auto",
            "mode": "one-vocoder",
            "retake": True,
            "bp_c_l": True,
            "adjust_lastword": 0
        }
    ]
    # Proxy config
    proxy_url = "http://Laxfrdangt:npIFNBVm@103.171.1.93:8536"

    try:
        
        response = requests.post(url, headers=headers, json=payload, proxies={"https": proxy_url})

        print("✅ Request thành công:", response.status_code)
        response_json = response.json()
        print("✅ Request thành công:", response_json)
    except Exception as e:
        print(f"❌ Lỗi khi gửi request: {e}")

def main():
    for i in range(10):
        send_typecast_request()
        print(f"Request {i+1} sent.")
        time.sleep(3)  # Đúng async sleep, không block event loop
main()
