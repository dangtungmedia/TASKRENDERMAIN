import os, ssl, time, random, shutil, json, re, math, asyncio, logging, subprocess
import requests, websocket, edge_tts, yt_dlp, boto3
from datetime import timedelta, datetime
from urllib.parse import urlparse
from decimal import Decimal
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image, ImageDraw, ImageFont
from googletrans import Translator
from requests_toolbelt.multipart.encoder import MultipartEncoder
from tqdm import tqdm
from proglog import ProgressBarLogger
from dotenv import load_dotenv

# Celery
from celery import shared_task, Celery
from celery.signals import task_failure, task_revoked

# Custom modules
from .random_video_effect import random_video_effect_cython

# Environment variable loading
load_dotenv()

# Environment variables
SECRET_KEY = os.getenv('SECRET_KEY')
SERVER = os.getenv('SERVER')
ACCESS_TOKEN = None
failed_accounts = set()
valid_tokens = {}

def get_filename_from_url(url):
    return os.path.basename(url.split('?')[0])

async def download_image(url, data, semaphore):
    video_id = data.get('video_id')
    async with semaphore:  # Giới hạn số lượng tác vụ đồng thời
        filename = get_filename_from_url(url)
        local_directory = os.path.join('media', str(video_id), 'image')
        os.makedirs(local_directory, exist_ok=True)
        file_path = os.path.join(local_directory, filename)
        for attempt in range(5):  # Thử tải lại 5 lần nếu thất bại
            try:
                response = requests.get(url, stream=True, timeout=200)
                if response.status_code == 200:
                    with open(file_path, 'wb') as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                    print(f"Tải xuống thành công: {url}")
                    return True  # Trả về True nếu tải thành công
                else:
                    print(f"Trạng thái không thành công - {response.status_code} - URL: {url}")
            except requests.RequestException as e:
                print(f"Lỗi yêu cầu khi tải xuống {url}: {e}")
            except Exception as e:
                print(f"Lỗi không xác định khi tải xuống {url}: {e}")
        return False  # Trả về False nếu không thể tải xuống

async def render_video_async(data, image_urls):
    video_id = data.get('video_id')
    semaphore = asyncio.Semaphore(20)  # Giới hạn 20 tác vụ đồng thời
    tasks = [download_image(url, data, semaphore) for url in image_urls]
    await asyncio.gather(*tasks)
    return f"Downloaded {len(image_urls)} images"

@shared_task(bind=True, ignore_result=True, priority=0, name='render_video', time_limit=14200, queue='render_video_content')
def render_video(self, data):
    task_id = self.request.id
    worker_id = self.request.hostname
    print(f"Task {task_id} running on worker {worker_id}")

    images = []
    text = data.get('text_content')
    text_entries = json.loads(text)
    for item in text_entries:
        video_url = item.get('url_video', "")
        if not video_url:
            return False
        parsed_url = urlparse(video_url)
        if parsed_url.scheme in ['http', 'https']:
            images.append(video_url)
        else:
            url = os.getenv('url_web') + video_url
            images.append(url)
    
    # Chạy Asyncio trong synchronous context (sử dụng Celery worker)
    asyncio.run(render_video_async(data, images))
    return f"Downloaded {len(images)} images"
