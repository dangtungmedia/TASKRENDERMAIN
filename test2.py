import requests
ip = requests.get("https://api.ipify.org").text
print("Public IP của bạn là:", ip)