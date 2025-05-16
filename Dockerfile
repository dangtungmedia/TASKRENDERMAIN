FROM python:3.12.10

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV TZ=Asia/Ho_Chi_Minh

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    ffmpeg \
    wget \
    python3-dev \
    unrar-free \
    libffi-dev \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Cài torch CUDA 12.1
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Cài Whisper từ GitHub chính thức
RUN pip install git+https://github.com/openai/whisper.git

# Optional: Add fonts if necessary
COPY fonts/* /usr/share/fonts/truetype/custom/

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app

