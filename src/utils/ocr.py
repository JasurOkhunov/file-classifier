from PIL import Image
from io import BytesIO
import pytesseract

def extract_text_from_image(file_bytes: bytes) -> str:
    try:
        image = Image.open(BytesIO(file_bytes))
        return pytesseract.image_to_string(image)
    except Exception as e:
        print(f"[OCR ERROR] {e}")
        return ""