# Python 3.9 slim imajı
FROM python:3.9-slim

WORKDIR /app

# ddddocr için gerekli temel kütüphaneler (libgl1 bazen gerekebilir)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]