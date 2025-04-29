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
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTg1NzhjNDg4MWRjMDVlYmYxOWExNWJhMjJkOGZkMWFiMzRjOGEiLCJ0eXAiOiJKV1QifQ.eyJfaWQiOiI2N2U2NjFkNTJmMmE2ZWQ0MDRjM2FjMjgiLCJhcHByb3ZlZCI6dHJ1ZSwiYXV0aHR5cGUiOiJmaXJlYmFzZSIsInByb3ZpZGVyIjoicGFzc3dvcmQiLCJpc19wYWlkIjpmYWxzZSwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3R5cGVjYXN0LXByb2QtNTBjYjEiLCJhdWQiOiJ0eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXV0aF90aW1lIjoxNzQ1OTEzOTg0LCJ1c2VyX2lkIjoiTmpXbTBBdDE4V1ZHaDBuVEdpUzBManBpVjRQMiIsInN1YiI6Ik5qV20wQXQxOFdWR2gwblRHaVMwTGpwaVY0UDIiLCJpYXQiOjE3NDU5MTM5ODQsImV4cCI6MTc0NTkxNzU4NCwiZW1haWwiOiJkdnMyMjg4OEBqaW9zby5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJkdnMyMjg4OEBqaW9zby5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJjdXN0b20ifX0.b-N9csLpf92Yl5Qwyv59pSF22KKOKldIwLhhweollMTmBezi9Hdc1c86hJdPqbSKoHrnlv9YnPitS85OPZkQ6mEwir44kl0SqAap_tqBF0T4xpbePNG4mHE9L8dtuFrYhYpwPxOKQm5uEPE_7LUwTKyFrDBaPZT7c5MZNI-WrM-GpNxQp41lmOVkHOd5cgTlMqYQmqp_kmr9k6CHUi9dphm0woJ_uSNjCy-15RNAhbOopgsRltljJBfiGdTMrJ1Iq7Ep4Yd2HDot_NHMiSqxWqMLLbAvWIFPV3er-dpX2ItZVxLjIZJSLowasMu2Hbka2DaWu9rQ2tSelrOtvms3fA",  # (token rút gọn)
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
