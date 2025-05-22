from io import BytesIO
from pdfminer.high_level import extract_text

def extract_text_from_pdf(file_bytes: bytes) -> str:
    try:
        buffer = BytesIO(file_bytes)
        text = extract_text(buffer)
        return text or ""
    except Exception as e:
        print(f"[ERROR] Failed to extract PDF text: {e}")
        return ""