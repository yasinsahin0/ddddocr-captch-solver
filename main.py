from fastapi import FastAPI
from pydantic import BaseModel
import base64
import ddddocr

app = FastAPI()

# OCR nesnesini global olarak başlatıyoruz (Her istekte tekrar yüklenmesin diye)
ocr = ddddocr.DdddOcr(show_ad=False)

class CaptchaRequest(BaseModel):
    image_base64: str

@app.post("/solve")
async def solve_captcha(request: CaptchaRequest):
    try:
        # 1. Base64 temizliği
        if "," in request.image_base64:
            base64_data = request.image_base64.split(",")[1]
        else:
            base64_data = request.image_base64

        # 2. Binary veriye çevir
        image_bytes = base64.b64decode(base64_data)

        # 3. ddddocr ile çözüm (Görüntü işlemeye gerek yok, ham veri verilir)
        res = ocr.classification(image_bytes)
        
        return {
            "status": "success", 
            "result": res
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/")
def read_root():
    return {"message": "ddddocr API Calisiyor"}