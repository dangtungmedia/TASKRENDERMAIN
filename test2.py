import requests




import requests
from fake_useragent import UserAgent

headers = {
    'Authorization': f'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ3YWU0OWM0YzlkM2ViODVhNTI1NDA3MmMzMGQyZThlNzY2MWVmZTEiLCJ0eXAiOiJKV1QifQ.eyJfaWQiOiI2N2U0YmM3MWQ3NDQ3ZWZlMmVmODM0MWIiLCJhcHByb3ZlZCI6dHJ1ZSwiYXV0aHR5cGUiOiJmaXJlYmFzZSIsInByb3ZpZGVyIjoicGFzc3dvcmQiLCJpc19wYWlkIjpmYWxzZSwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3R5cGVjYXN0LXByb2QtNTBjYjEiLCJhdWQiOiJ0eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXV0aF90aW1lIjoxNzUyNDcxMTg3LCJ1c2VyX2lkIjoic2dhcGZXZXBrY1h4QndXSEJEYmN6cHpzcG11MiIsInN1YiI6InNnYXBmV2Vwa2NYeEJ3V0hCRGJjenB6c3BtdTIiLCJpYXQiOjE3NTI0NzExODcsImV4cCI6MTc1MjQ3NDc4NywiZW1haWwiOiJnY2M1NzEwMUBqaW9zby5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJnY2M1NzEwMUBqaW9zby5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJjdXN0b20ifX0.3TBcftt8Nmqv3pW8jZXk8Bs4dxZKbLu2-s0hZFNEA--C9P0vOT0nx_iBmFKpklxLlmo6iPPD3ynRNpVDbSyGyZxIyOLdNwF-XkcqeWeT43pGdG9XYghYPkASlN-UYtdJNck0rWYw6WOKgSFqQNjSob21AzQh5rUT5emX9szbQnLCo3Ska0tB0UJL9zoX90C0xwKIVIlDMoGhc9-6Qv4cbDQUHoimxv33Z_OSvRXfIX-hiNncftnIgckj946OmuU1rZpWElIbpYzTkLJnU6FP89-fQHbRjPjaCvugvscOePpF0LF9I3y9lZIeyWXrPh_cu-RqhV6fOqwN9LcZIUPiVA', 
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

print(f"Response content: {response.json()}")
