import time
import logging
from threading import Lock, Thread
import websocket
import json


class WebSocketClient:
    def __init__(self, url, min_delay=1.0):
        self.url = url
        self.ws = None
        self.lock = Lock()
        self.last_send_time = 0
        self.min_delay = min_delay
        
        # Status messages that bypass rate limiting
        self.important_statuses = [
            "Render Thành Công : Đang Chờ Upload lên Kênh",
            "Đang Render : Upload file File Lên Server thành công!",
            "Đang Render : Đang xử lý video render",
            "Đang Render : Đã lấy thành công thông tin video reup",
            "Render Lỗi"
        ]
        self.logger = self._setup_logger()

    def _setup_logger(self):
        """Setup logging configuration"""
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        return logger
        
    def should_send(self, status):
        """Check if message should be sent based on status and rate limiting"""
        current_time = time.time()
        time_since_last = current_time - self.last_send_time

        # Check if status contains any important keywords
        if status and any(keyword in status for keyword in self.important_statuses):
            return True
            
        # Apply rate limiting for other statuses
        return time_since_last >= self.min_delay
        
    def connect(self):
        """Establish WebSocket connection"""
        try:
            if self.ws is None or not self.ws.connected:
                self.ws = websocket.WebSocket()
                self.ws.settimeout(30)
                self.ws.connect(self.url)
                self.logger.info("Successfully connected to WebSocket")
                return True
        except Exception as e:
            self.logger.error(f"Connection failed: {str(e)}")
            return False

    def send(self, data, max_retries=5):
        """Send data through WebSocket with rate limiting and retries"""
        with self.lock:
            try:
                status = data.get('status')
                
                if not self.should_send(status):
                    return True
                    
                for attempt in range(max_retries):
                    try:
                        if not self.ws or not self.ws.connected:
                            if not self.connect():
                                sleep_time = min(2 * attempt + 1, 10)
                                time.sleep(sleep_time)
                                continue
                                
                        self.ws.send(json.dumps(data))
                        self.last_send_time = time.time()
                        self.logger.debug(f"Successfully sent message: {status}")
                        return True
                        
                    except websocket.WebSocketTimeoutException:
                        self.logger.error(f"Timeout on attempt {attempt + 1}")
                        self.ws = None
                    except Exception as e:
                        self.logger.error(f"Send failed: {str(e)}")
                        self.ws = None
                        
                    sleep_time = min(2 * attempt + 1, 10)
                    time.sleep(sleep_time)
                
                self.logger.error(f"Failed to send after {max_retries} attempts")
                return False
                
            except Exception as e:
                self.logger.error(f"Error in send method: {str(e)}")
                return False
                
    def close(self):
        """Close WebSocket connection"""
        try:
            if self.ws:
                self.ws.close()
                self.logger.info("WebSocket connection closed")
        except Exception as e:
            self.logger.error(f"Error closing connection: {str(e)}")

# Khởi tạo WebSocket client một lần
ws_client = WebSocketClient("wss://hrmedia89.com/ws/update_status/")
            
data = {
        "type": 'update-status',
        'video_id': 16199,
        'status': "test thử 115555",
        'task_id': "",
        'worker_id': "",
        "url_thumbnail": "",
        'title': "",
        'url_video':"",
        "secret_key": "ugz6iXZ.fM8+9sS}uleGtIb,wuQN^1J%EvnMBeW5#+CYX_ej&%"
    }

ws_client = WebSocketClient("wss://autospamnews.com/ws/update_status/")
ws_client.send(data)
