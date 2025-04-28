import time
import aiohttp
import asyncio
import json
from fake_useragent import UserAgent

print("test")

async def send_typecast_request():
    url = "https://typecast.ai/api/speak/batch/post"
    ua = UserAgent()

    headers = {
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjNmOWEwNTBkYzRhZTgyOGMyODcxYzMyNTYzYzk5ZDUwMjc3ODRiZTUiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVHVuZyBkYW5nIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FHTm15eGIzZWg4cjAzYmNqRkxkT3ZIcFpNeDZPOWR3TVdFYWk3X18tWXdLPXM5Ni1jIiwiX2lkIjoiNjQ1NTQ0ZDFiYzI5M2FhYjQzZmZhMWE2IiwiYXBwcm92ZWQiOnRydWUsImF1dGh0eXBlIjoiZmlyZWJhc2UiLCJwcm92aWRlciI6InBhc3N3b3JkIiwiaXNfcGFpZCI6ZmFsc2UsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS90eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXVkIjoidHlwZWNhc3QtcHJvZC01MGNiMSIsImF1dGhfdGltZSI6MTc0NTgzNDE3NCwidXNlcl9pZCI6Ikc1RjhwdHFiT2VUQnlOMVdDeXRyamp0ZVhkZDIiLCJzdWIiOiJHNUY4cHRxYk9lVEJ5TjFXQ3l0cmpqdGVYZGQyIiwiaWF0IjoxNzQ1ODM0MTc0LCJleHAiOjE3NDU4Mzc3NzQsImVtYWlsIjoiZGFuZ3R1bmdtZWRpYUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJkYW5ndHVuZ21lZGlhQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6ImN1c3RvbSJ9fQ.MYJ-AqsUkVwc691IgHeVgCQaDAatgzjJlsHkwO2vxO9ZCHxptJlllHIgZ-kQkUFGYZ8KX1MR0YwkkpnXv6NBtLSjZx-ldUObiaCuYOffDbNDIr5no_StzqwmvS5gGsruSuU3nH8jNFju18eMX0y3EqZ8ofZe_pITPduGqOifT0bMDTZX1U-DPGsQyt12N--Sz9rr5fc6nd0UaslgttEG8UCAiJL0hIuDbHkd4-57_jrMBPb4EfJ3tdxYK4P-qlKbxWJk8him8bQoc6XsvutH2rI9HMcYPCKL4beEAODY7ObJ02r5TrkrE209KPpmmv9t40h7IvaUkmFta5jtJDPNtA",  # (token rút gọn)
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
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url,
                headers=headers,
                json=payload,
                # proxy=proxy_url,
                ssl=False  # ⚡ RẤT QUAN TRỌNG: Bỏ SSL verify qua proxy
            ) as response:
                print(f"Status code: {response.status}")
                response_text = await response.text()
                print(f"Response: {response_text}")

    except Exception as e:
        print(f"❌ Lỗi khi gửi request: {e}")

async def main():
    for i in range(10):
        await send_typecast_request()
        print(f"Request {i+1} sent.")
        await asyncio.sleep(3)  # Đúng async sleep, không block event loop


asyncio.run(main())
