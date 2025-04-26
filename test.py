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
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTg1NzhjNDg4MWRjMDVlYmYxOWExNWJhMjJkOGZkMWFiMzRjOGEiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVHVuZyBkYW5nIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FHTm15eGIzZWg4cjAzYmNqRkxkT3ZIcFpNeDZPOWR3TVdFYWk3X18tWXdLPXM5Ni1jIiwiX2lkIjoiNjQ1NTQ0ZDFiYzI5M2FhYjQzZmZhMWE2IiwiYXBwcm92ZWQiOnRydWUsImF1dGh0eXBlIjoiZmlyZWJhc2UiLCJwcm92aWRlciI6InBhc3N3b3JkIiwiaXNfcGFpZCI6ZmFsc2UsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS90eXBlY2FzdC1wcm9kLTUwY2IxIiwiYXVkIjoidHlwZWNhc3QtcHJvZC01MGNiMSIsImF1dGhfdGltZSI6MTc0NTY0ODk0OSwidXNlcl9pZCI6Ikc1RjhwdHFiT2VUQnlOMVdDeXRyamp0ZVhkZDIiLCJzdWIiOiJHNUY4cHRxYk9lVEJ5TjFXQ3l0cmpqdGVYZGQyIiwiaWF0IjoxNzQ1NjQ4OTQ5LCJleHAiOjE3NDU2NTI1NDksImVtYWlsIjoiZGFuZ3R1bmdtZWRpYUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJkYW5ndHVuZ21lZGlhQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6ImN1c3RvbSJ9fQ.VmRa1_2NmlMPenlVqzU-gNunR9ufuLgHo3B941E0wLyiObIphlRgKYymnf3KMmEEsbhDlt9WdNMXGFdk-4U6tdjbSaOjVylK20K4xV8awjbOdoRxQ7L2lG1TIIBrwFhEJ7plJFNrLspKyb7mRXUtPunsYTWt-OORqgK-Fm5E6_zwTQ-k90H2AiAJBWe5YW5HscrtYgdZVYw3MhT_vmc0yWqpz3TFABDHjy90-kDp_k8ExdjoX8L0v-XmC_Qabxy_piWTLAxGQ0Lam5WWU4DzQZ17F1sj1xs8VTBSrEzMAWVPVgkYhoPi-uLnGmqkCcf22vkHyInCBREcCDBjvVBPkQ",
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
        "https": "http://dangtmunZh:0auVrCMq@103.167.92.214:8943",
    }
    # Gửi request
    try:
        # Thử nhiều cách gửi request
        print("\n--- Phương pháp 1: Gửi payload dạng string ---")
        response1 = requests.post(url, headers=headers, data=payload_str, verify=False,proxies=proxies,timeout=10)
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


 
                    