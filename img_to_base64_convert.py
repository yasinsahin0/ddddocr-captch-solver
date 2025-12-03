import base64
import requests
import os
import json

# 1. AYARLAR
API_URL = "http://localhost:8000/solve"
IMAGE_FILENAME = "cap1.png" # Klasördeki dosya adı

def main():
    # 2. Resim yolunu dinamik bulma
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "images", IMAGE_FILENAME)

    print(f"🖼️  İşlenen Resim: {image_path}")

    # Dosya kontrolü
    if not os.path.exists(image_path):
        print("❌ HATA: Resim dosyası bulunamadı!")
        return

    # 3. Resmi Base64'e Çevirme
    try:
        with open(image_path, "rb") as image_file:
            # Base64'e çevir ve string formatına getir
            b64_string = base64.b64encode(image_file.read()).decode('utf-8')
            print("✅ Base64 dönüşümü başarılı.")
    except Exception as e:
        print(f"❌ Dosya okuma hatası: {e}")
        return

    # 4. API'ye İstek Gönderme
    payload = {
        "image_base64": b64_string
    }

    print(f"📡 API'ye bağlanılıyor: {API_URL} ...")
    
    try:
        response = requests.post(API_URL, json=payload)
        
        # 5. Sonucu Yazdırma
        if response.status_code == 200:
            data = response.json()
            print("\n" + "="*40)
            print("🎯 SONUÇ BAŞARILI!")
            print("="*40)
            # JSON verisini güzel formatta yazdıralım
            print(json.dumps(data, indent=4))
            
            # Sadece çözülen metni gösterelim
            print("-" * 20)
            print(f"🔠 ÇÖZÜLEN METİN: {data.get('result', 'Bulunamadı')}")
            print("-" * 20)
        else:
            print(f"⚠️ HATA: API {response.status_code} kodu döndürdü.")
            print(response.text)

    except requests.exceptions.ConnectionError:
        print("❌ BAĞLANTI HATASI: Docker konteynerinin çalıştığından emin misin?")
        print("   'docker ps' yazarak kontrol et.")

if __name__ == "__main__":
    main()