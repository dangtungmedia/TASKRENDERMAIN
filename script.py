import time
import aiohttp
import asyncio
import json
from fake_useragent import UserAgent
import requests
print("test")

async def send_typecast_request():
    url = "https://typecast.ai/api/speak/batch/post"
    ua = UserAgent()

    headers = {
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjNmOWEwNTBkYzRhZTgyOGMyODcxYzMyNTYzYzk5ZDUwMjc3ODRiZTUiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVHVuZyBkYW5nIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FHTm15eGIzZWg4cjAzYmNqRkxkT3ZIcFpNeDZPOWR3TVdFYWk3X18tWXdLPXM5Ni1jIiwiX2lkIjoiNjQ1NTQ0ZDFiYzI5M2FhYjQzZmZhMWE2IiwiYXBwcm92ZWQiOnRydWUsImF1dGh0eXBlIjoiZmlyZWJhc2UiLCJwcm92aWRlciI6InBhc3N3b3JkIiwiaXNfcGFpZCI6ZmFsc2UsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS90eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXVkIjoidHlwZWNhc3QtcHJvZC01MGNiMSIsImF1dGhfdGltZSI6MTc0NTgzODIxMiwidXNlcl9pZCI6Ikc1RjhwdHFiT2VUQnlOMVdDeXRyamp0ZVhkZDIiLCJzdWIiOiJHNUY4cHRxYk9lVEJ5TjFXQ3l0cmpqdGVYZGQyIiwiaWF0IjoxNzQ1ODM4MjEyLCJleHAiOjE3NDU4NDE4MTIsImVtYWlsIjoiZGFuZ3R1bmdtZWRpYUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJkYW5ndHVuZ21lZGlhQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6ImN1c3RvbSJ9fQ.ChJeME45NFFz185gGht-oyYopwiYxgK0tTLiuSEZAdwn1KFEvOk7w5KLD_JwDnWSAi3adGYLY5xYhS8-6l0Q8o-5QrthwD12OUjo1Jl2I6aAEMripq_4bXeKAkb6WbNPTwf5ZqKWgV9PBNq_s-x1oaX3cWelivp9j5fxwoUiGMa0rlgm-lcK5aIUYWaq9XDv5UVHj4U3-158hmaDgx92c1gcBQqZ5jfKUNAK4DeKFLQi0pf9kN_JIMYsGDPrhkdilLSekuKg4SLxOSb90mW8ns56YwS8zuwiXMvikpXJa8RekOixDegWYvv_LVq0BDV6s5420njhFnnCbfsb7wPnKA",  # (token rút gọn)
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
    proxy_url = "http://dangtw9tnW:lAlmH2qG@103.74.107.58:8311"

    try:
        
        response = requests.post(url, headers=headers, json=payload, proxies={"https": proxy_url})

        print("✅ Request thành công:", response.status_code)
        response_json = response.json()
        print("✅ Request thành công:", response_json)
    except Exception as e:
        print(f"❌ Lỗi khi gửi request: {e}")

async def main():
    for i in range(10):
        await send_typecast_request()
        print(f"Request {i+1} sent.")
        await asyncio.sleep(3)  # Đúng async sleep, không block event loop
asyncio.run(main())
