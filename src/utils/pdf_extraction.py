from io import BytesIO
from pdfminer.high_level import extract_text

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extracts text content from a PDF file provided as bytes.

    Args:
        file_bytes (bytes): The PDF file content in bytes.

    Returns:
        str: The extracted text from the PDF, or an empty string if extraction fails.

    Raises:
        None: All exceptions are caught and handled internally.
    """
    try:
        buffer = BytesIO(file_bytes)
        text = extract_text(buffer)
        return text or ""
    except Exception as e:
        print(f"[ERROR] Failed to extract PDF text: {e}")
        return ""