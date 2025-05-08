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
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjU5MWYxNWRlZTg0OTUzNjZjOTgyZTA1MTMzYmNhOGYyNDg5ZWFjNzIiLCJ0eXAiOiJKV1QifQ.eyJfaWQiOiI2N2U0YjhlOGFkOGE5ZDQ3OWU0NzFlNjYiLCJhcHByb3ZlZCI6dHJ1ZSwiYXV0aHR5cGUiOiJmaXJlYmFzZSIsInByb3ZpZGVyIjoicGFzc3dvcmQiLCJpc19wYWlkIjpmYWxzZSwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3R5cGU0YjhlOGFkOGE5ZDQ3OWU0NzFlNjYiLCJhcHByb3ZlZCI6dHJ1ZSwiYXV0aHR5cGUiOiJmaXJlYmFzZSIsInByb3ZpZGVyIjoicGFzc3dvcmQiLCJpc19wYWlkIjpmYWxzZSwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3R5cGVjYXN0LXByb2QtNTBjYjEiLCJhdWQiOiJ0eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXV0aF90aW1lIjoxNzQ2NzE1MTk1LCJ1c2VyX2lkIjoieUk1UFhvTU52cldEc0JrWTYzcTF3R3V1TVZtMSIsInN1YiI6InlJNVBYb01OdnJXRHNCa1k2M3Exd0d1dUVjYXN0LXByb2QtNTBjYjEiLCJhdWQiOiJ0eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXV0aF90aW1lIjoxNzQ2NzE1MTk1LCJ1c2VyX2lkIjoieUk1UFhvTU52cldEc0JrWTYzcTF3R3V1TVZtMSIsInN1YiI6InlJNVBYb01OdnJXRHNCa1k2M3Exd0d1dU1WbTEiLCJpYXQiOjE3NDY3MTUxOTUsImV4cCI6MTc0NjcxODc5NSwiZW1haWwiOiJlcW4yNjk0M0BqaW9zby5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJlcW4yNjk0M0BqaW9zby1WbTEiLCJpYXQiOjE3NDY3MTUxOTUsImV4cCI6MTc0NjcxODc5NSwiZW1haWwiOiJlcW4yNjk0M0BqaW9zby5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJlcW4yNjk0M0BqaW9zby5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJjdXN0b20ifX0.Cgpn473SHeIlbmET7tHz_l3W2WP6jsdJcuFeE-7ISaAAABLRVkuf7-NAeqq8_S78O3A2zWVSnBeXFGnJbhxy0jaYAAeMeGXTfyh-AH0ojA6nuzNB8LUUZhMx-t0Xhq3t-gyswKmx_H-S99rxNtkzVkeK2hy2FCg_OBI6KuDWV9toxQql196xxmg_Nv4mdOUhdzRNCwDGJmqF1b-trNV0z9cD1r837dMgSMLbSkJyO9bLY6Eb4P3yDcbBfNbJlF4GjeMdfvk55MEQRNB9siZSL7rMD6vOe32mkz31EJsrp8FNeOhciHqvFV3O_nZ03tEskf3fJtuV8ko1kN4bOBcSww",  # (token rút gọn)
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
    proxy_url = "http://zbaUmdangt:l5wbPok2@103.171.1.93:8362"

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
