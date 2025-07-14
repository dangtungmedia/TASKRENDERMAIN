import requests




import requests
from fake_useragent import UserAgent

headers = {
    'Authorization': f'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ3YWU0OWM0YzlkM2ViODVhNTI1NDA3MmMzMGQyZThlNzY2MWVmZTEiLCJ0eXAiOiJKV1QifQ.eyJfaWQiOiI2N2U0YmU0ZmViMTI5N2MzYzkwNTU5YTEiLCJhcHByb3ZlZCI6dHJ1ZSwiYXV0aHR5cGUiOiJmaXJlYmFzZSIsInByb3ZpZGVyIjoicGFzc3dvcmQiLCJpc19wYWlkIjpmYWxzZSwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3R5cGVjYXN0LXByb2QtNTBjYjEiLCJhdWQiOiJ0eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXV0aF90aW1lIjoxNzUyNDY2MTM5LCJ1c2VyX2lkIjoiWEl2NGlMT2lVMWdsYjJLRE9vc29Qb3R3cnhFMyIsInN1YiI6IlhJdjRpTE9pVTFnbGIyS0RPb3NvUG90d3J4RTMiLCJpYXQiOjE3NTI0NjYxMzksImV4cCI6MTc1MjQ2OTczOSwiZW1haWwiOiJmbGQ2OTMwN0BiY29vcS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJmbGQ2OTMwN0BiY29vcS5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJjdXN0b20ifX0.FH5uHrwicNyWAWV2luoFjbwexEQkBI9RuWRrZGuR_xWjvwW1oeDchDHaXqxF3edEU3DjXsD6h1LzXrzV_s_gvpnpXhhESVwkAcGUFNq8_DjbvfMia4uUrATvopKIs1Xj0A43VQQiADS0FHa6tTmJbYmIU8qc6aNMK1_AdZa3G0ATXK0LoFZcbV8uN2xID2nh75qdcR1cET5hHqaHX8NHco9hWwcXNleaWbq91y5FpWTWMnLLOQFu0aooFQZfGMfJwFsPex_tOri5PZ-19--BY0zp5JTvPEcLQHSW8o5WdvdWMi2E0ktOaPKY5YuU1tFuf_iDUd3dM5d8_1ljWVtD4A', 
    'Content-Type': 'application/json',
    "User-Agent": UserAgent().google
}
url = "https://typecast.ai/api/speak/batch/post"
proxy_url = "http://Laxfrdangt:npIFNBVm@103.171.1.93:8536"

style_name_data=[
  {
    "text": "이재명 정부 초대 장관 후보자들의 인사청문회 '슈퍼 위크'가 시작됐습니다.",
    "actor_id": "66f4ecb5b1a24ceec9f6ccf0",
    "tempo": 1,
    "pitch": 0,
    "style_label": "normal-1",
    "style_label_version": "v3",
    "emotion_label": "happy",
    "emotion_scale": 1,
    "lang": "eng",
    "mode": "one-vocoder",
    "retake": True,
    "bp_c_l": True,
    "adjust_lastword": 0
  }
]

response = requests.post(url, headers=headers, json=style_name_data, proxies={"https": proxy_url})

print(f"Response status code: {response.status_code}")