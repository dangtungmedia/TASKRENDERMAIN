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
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjNmOWEwNTBkYzRhZTgyOGMyODcxYzMyNTYzYzk5ZDUwMjc3ODRiZTUiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVHVuZyBkYW5nIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FHTm15eGIzZWg4cjAzYmNqRkxkT3ZIcFpNeDZPOWR3TVdFYWk3X18tWXdLPXM5Ni1jIiwiX2lkIjoiNjQ1NTQ0ZDFiYzI5M2FhYjQzZmZhMWE2IiwiYXBwcm92ZWQiOnRydWUsImF1dGh0eXBlIjoiZmlyZWJhc2UiLCJwcm92aWRlciI6InBhc3N3b3JkIiwiaXNfcGFpZCI6ZmFsc2UsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS90eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXVkIjoidHlwZWNhc3QtcHJvZC01MGNiMSIsImF1dGhfdGltZSI6MTc0NTc2NjA4OSwidXNlcl9pZCI6Ikc1RjhwdHFiT2VUQnlOMVdDeXRyamp0ZVhkZDIiLCJzdWIiOiJHNUY4cHRxYk9lVEJ5TjFXQ3l0cmpqdGVYZGQyIiwiaWF0IjoxNzQ1NzY2MDg5LCJleHAiOjE3NDU3Njk2ODksImVtYWlsIjoiZGFuZ3R1bmdtZWRpYUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJkYW5ndHVuZ21lZGlhQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6ImN1c3RvbSJ9fQ.XfgoBk28RSC6EtCVlKnrecb6JZXQVk1ckQHUyhRW9iUjb7fPAlFa8geL92h-1jP8ul2MxVFOZHyjm6LVBruChyzuUaa9ULdtzrJQQY5kb7Y5QKeNE8UVCZmxlJBPYpKBnZFuDmNFDxrFOhfC1ZoXKNaB6-zumfj1vO1GZqlw3fUIx9qeLyKClrgrjRRRPLosoaPSzOxbFWpVr8pkkGZMczUfFSzKZE6lzw5q2RKhpa-PobEzrAP_XeLAzK0sLmQ76zaA2BDSk9tRB9ZeHfrhofmecWZXunvSSJaYx9k1HWbRDJaSbST1SVg2RmmHw6ztrKDGyn8xnsyd-3Ozc9AFTQ",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        
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
    
    proxies = {
        "https": "http://dangt3VmKX:TjVYTQ04@36.50.52.132:8227",
    }
    # Gửi request
    try:
        # Thử nhiều cách gửi request
        print("\n--- Phương pháp 1: Gửi payload dạng string ---")
        response1 = requests.post(url, headers=headers, data=payload_str, verify=False,proxies=proxies)
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

    # repose = requests.get("https://api.zingproxy.com/getip/us/f49740492df909e449ba33bfb8585f435041bc6b")

    # print(repose.text)
    # print(repose.json())


 
                    