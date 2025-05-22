import pytesseract
from PIL import Image
import io
import logging

def extract_text_from_image(image_bytes: bytes) -> str:
    try:
        image = Image.open(io.BytesIO(image_bytes))

        # Resize to improve performance on render
        MAX_DIM = 1000
        image.thumbnail((MAX_DIM, MAX_DIM), Image.Resampling.LANCZOS)

        # Run OCR with timeout
        text = pytesseract.image_to_string(image, timeout=10)
        logging.info(f"[OCR] Extracted text: {text[:100]}")
        return text
    except Exception as e:
        logging.error(f"[OCR] Error: {e}")
        return ""