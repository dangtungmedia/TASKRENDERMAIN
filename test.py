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
                    "Đang Render : Đã chọn xong video nối",
                    "Render Lỗi"
                ]
            
    def should_send(self, status):
        """Check if message should be sent based on status and rate limiting"""
        current_time = time.time()
        time_since_last = current_time - self.last_send_time

        if status in self.important_statuses:
            return True
            
        return time_since_last >= self.min_delay
        
    def connect(self):
        """Establish WebSocket connection"""
        try:
            if self.ws is None or not self.ws.connected:
                self.ws = websocket.WebSocket()
                self.ws.connect(self.url)
                return True
        except Exception as e:
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
                                self.logger.warning(f"Connection attempt {attempt + 1} failed")
                                continue
                                
                        self.ws.send(json.dumps(data))
                        self.last_send_time = time.time()
                        self.logger.debug(f"Successfully sent message: {status}")
                        return True
                        
                    except Exception as e:
                        self.logger.error(f"Send attempt {attempt + 1} failed: {str(e)}")
                        time.sleep(1)
                        continue
                        
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

def update_status_video(status_video, video_id, task_id, worker_id, url_thumnail=None, url_video=None, title=None, id_video_google=None):
    """Cập nhật trạng thái video lên server."""
    data = {
        'action': 'update_status',
        'video_id': video_id,
        'status': status_video,
        'task_id': task_id,
        'worker_id': worker_id,
        "url_thumnail": url_thumnail,
        'title': title,
        'url_video': url_video,
        'id_video_google': id_video_google,
    }
    return ws_client.send(data) 