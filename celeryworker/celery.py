from celery import Celery
import os
from dotenv import load_dotenv
load_dotenv()

# Tạo ứng dụng Celery với tên 'celeryworker'
app = Celery('celeryworker')

# Tự động tìm kiếm và nạp các task từ các module chỉ định trong package 'celeryworker'
app.autodiscover_tasks(['celeryworker'])

# Thiết lập timezone cho Celery
app.conf.timezone = 'Asia/Ho_Chi_Minh'  # Sử dụng đúng cú pháp với chữ hoa
broker_url  =  os.environ.get('CELERY_BROKER_URL', 'redis://127.0.0.1:6379/0' )
result_backend  = os.environ.get('CELERY_RESULT_BACKEND', 'redis://127.0.0.1:6379/0')

