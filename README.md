
````markdown
# 🧩 Dockerized Captcha Solver API (ddddocr)

Bu proje, Base64 formatında gelen CAPTCHA görüntülerini çözümleyerek metin halini döndüren, **FastAPI** ve **ddddocr** (Derin Öğrenme tabanlı OCR) kullanılarak hazırlanmış, Dockerize edilmiş bir mikro servistir.

Tesseract gibi geleneksel OCR yöntemlerine göre CAPTCHA çözmede çok daha yüksek başarı oranına sahiptir.

## 📂 Proje Yapısı

Dosyaların şu şekilde organize edildiğinden emin olun:

```text
captcha-solver/
├── Dockerfile          # Docker imaj konfigürasyonu
├── main.py             # FastAPI uygulama kodu
├── requirements.txt    # Python bağımlılıkları
└── README.md           # Bu dosya
````

-----

## 🚀 Kurulum ve Çalıştırma

Aşağıdaki adımları terminalde proje klasörünün içindeyken uygulayın.

### 1\. Docker İmajını Oluşturma (Build)

Önce projeyi bir Docker imajı haline getirmemiz gerekiyor. Bu işlem kütüphaneleri indirip kuracağı için ilk seferde birkaç dakika sürebilir.

```bash
docker build -t ddddocr-captch-solver .
```

  * `-t captcha-api`: İmajımıza `captcha-api` ismini verir.
  * `.`: `Dockerfile`'ın bulunduğu mevcut dizini işaret eder.

### 2\. Konteyneri Başlatma (Run)

İmaj oluşturulduktan sonra konteyneri ayağa kaldırın:

```bash
docker run -d -p 8000:8000 --name ddddocr-captcha-container --restart unless-stopped ddddocr-captch-solver
```

  * `-d`: Arka planda (detach mode) çalıştırır.
  * `-p 8000:8000`: Konteynerin 8000 portunu makinenizin 8000 portuna bağlar.
  * `--name captcha-container`: Konteynere bir isim verir.
  * `--restart unless-stopped`: Konteyner çökerse veya bilgisayar yeniden başlarsa otomatik tekrar başlatır.

-----

## 📡 Kullanım (API Endpoints)

API şu anda `http://localhost:8000` adresinde çalışmaktadır.

### 1\. Health Check (Kontrol)

Servisin çalışıp çalışmadığını test etmek için:

  * **URL:** `GET http://localhost:8000/`
  * **Yanıt:** `{"message": "ddddocr API Calisiyor"}`

### 2\. CAPTCHA Çözme

  * **URL:** `POST http://localhost:8000/solve`

  * **Content-Type:** `application/json`

  * **Body:**

    ```json
    {
      "image_base64": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
    }
    ```

    *(Not: Base64 string'i başında 'data:image...' olsa da olmasa da çalışır.)*

  * **Başarılı Yanıt:**

    ```json
    {
      "status": "success",
      "result": "xy92"
    }
    ```

-----

## 🧪 Test Etme Yöntemleri

### Yöntem A: cURL ile Test (Terminal)

```bash
curl -X 'POST' \
  'http://localhost:8000/solve' \
  -H 'Content-Type: application/json' \
  -d '{
  "image_base64": "BURAYA_CAPTCHA_BASE64_KODUNU_YAPISTIRIN"
}'
```

### Yöntem B: Python Script ile Test

```python
import requests
import base64

# Örnek: Yerel bir resmi test etmek için
with open("ornek_captcha.jpg", "rb") as image_file:
    b64_string = base64.b64encode(image_file.read()).decode('utf-8')

url = "http://localhost:8000/solve"
payload = {"image_base64": b64_string}

response = requests.post(url, json=payload)
print(response.json())
```

### Yöntem C: Swagger UI (Tarayıcı)

Tarayıcınızda şu adrese gidin:
[http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)

Buradan görsel arayüz ile test yapabilirsiniz.

-----

## 🛠 Yönetim Komutları

**Logları izlemek için (Hata ayıklama):**

```bash
docker logs -f captcha-container
```

**Konteyneri durdurmak için:**

```bash
docker stop captcha-container
```

**Konteyneri silmek için:**

```bash
docker rm captcha-container
```

**İmajı silmek için (Yer açmak isterseniz):**

```bash
docker rmi captcha-api
```

```
```