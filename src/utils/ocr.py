import pytesseract
from PIL import Image
import io
import logging

def extract_text_from_image(image_bytes: bytes) -> str:
    """
    Extracts text from an image using OCR (Optical Character Recognition).

    Args:
        image_bytes (bytes): The image data in bytes.

    Returns:
        str: The text extracted from the image. Returns an empty string if extraction fails.

    Notes:
        - The image is resized to a maximum dimension of 1000 pixels to improve OCR performance.
        - OCR is performed with a timeout of 10 seconds.
        - Logs extracted text (up to 100 characters) and errors.
    """
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