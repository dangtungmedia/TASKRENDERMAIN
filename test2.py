import time
import aiohttp
import asyncio
import json
from fake_useragent import UserAgent
import requests

url = "https://api.ipify.org/"
proxy_url = "http://zbaUmdangt:l5wbPok2@103.171.1.93:8362"

response = requests.get(url,proxies={"https": proxy_url})

print(response.status_code)
print(response.text)
print("test")