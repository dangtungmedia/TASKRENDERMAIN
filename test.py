import aiohttp
import asyncio
import json
from fake_useragent import UserAgent

async def send_typecast_request():
    url = "https://typecast.ai/api/speak/batch/post"
    ua = UserAgent()
    
    headers = {
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTg1NzhjNDg4MWRjMDVlYmYxOWExNWJhMjJkOGZkMWFiMzRjOGEiLCJ0eXAiOiJKV1QifQ.eyJfaWQiOiI2N2U0YzBhN2E0YjQyOTVkZGQ0NGYxYWIiLCJhcHByb3ZlZCI6dHJ1ZSwiYXV0aHR5cGUiOiJmaXJlYmFzZSIsInByb3ZpZGVyIjoicGFzc3dvcmQiLCJpc19wYWlkIjpmYWxzZSwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3R5cGVjYXN0LXByb2QtNTBjYjEiLCJhdWQiOiJ0eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXV0aF90aW1lIjoxNzQ1ODE5ODM0LCJ1c2VyX2lkIjoiRE1ta0tsY0lFcFcyOVRhN3BaTU5DbDVMWHE0MyIsInN1YiI6IkRNbWtLbGNJRXBXMjlUYTdwWk1OQ2w1TFhxNDMiLCJpYXQiOjE3NDU4MTk4MzQsImV4cCI6MTc0NTgyMzQzNCwiZW1haWwiOiJlYmM3NDA3MEBiY29vcS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJlYmM3NDA3MEBiY29vcS5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJjdXN0b20ifX0.KnzIvtIYPNSGUcny1DaSZXEdbH3FiV0SYbpLG_DBQD1GxhZz5Nx3Fd6_mQ9bi0Tep0QYs_gKYb1It5J7QzlVU08Eq3Bk5nL31UMB8_9D5nI-e2WNc3NAOKoGZSk6lzBcqINl3EExg2jFfVw9T4UnMk7VPVrOYA0yxu2ElZC-3eoC1MQFGqm0nZUrbdyyMLT-nyBk6LbLgFtwCqHzRTeaL8cv9GlPvrNc7mol8c_05E1ix6jcVTVhrWTsRDlwbR-T_zeBSZIQ1IIhDIB2SVYBipld_LjTk37hYlN-ZaXZpRkDfWcacIgdgx9-jSo2CQF6NSyKoCInhBcmEKljmhGsww",  # (rút gọn)
        "Content-Type": "application/json",
        "User-Agent": ua.google
    }

    payload = [
        {
            "text": "hello my nam is tung 1 2 3 4 5 6 7 8 9 10",
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

    proxy_url = "http://dangtw9tnW:lAlmH2qG@103.74.107.58:8311"  # nếu muốn dùng proxy

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url,
            headers=headers,
            json=payload,
            proxy=proxy_url  # hoặc bỏ dòng này nếu không cần proxy
        ) as response:
            print(f"Status code: {response.status}")
            response_text = await response.text()
            print(f"Response: {response_text}")

# Chạy async
if __name__ == "__main__":
    asyncio.run(send_typecast_request())
