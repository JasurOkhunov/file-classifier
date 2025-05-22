from werkzeug.datastructures import FileStorage
from src.utils.office_extraction import (
    extract_text_from_docx,
    extract_text_from_xlsx   
)
from src.utils.csv_extraction import extract_text_from_csv
from src.utils.txt_extraction import extract_text_from_txt
from src.utils.pdf_extraction import extract_text_from_pdf
from src.utils.ocr import extract_text_from_image
from src.utils.util import (
    classify_with_model,
    clean_text,
    is_bank_statement,
    is_invoice,
    is_driver_license
)
import logging
logging.basicConfig(level=logging.INFO)

# MAIN CLASSIFICATION LOGIC
def classify_file(file: FileStorage) -> str:
    filename = file.filename.lower().strip()
    file_bytes = file.read()
    logging.info(f"File received: {filename}")

    # STEP 1: Try basic filename-based classification (cheap)
    if "driver" in filename or "drivers_license" in filename or "driver_license" in filename:
        return "driver license"
    if "bank" in filename or "bank_statement" in filename:
        return "bank statement"
    if "invoice" in filename:
        return "invoice"

    # STEP 2: Extract content based on file type
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_bytes)
    elif filename.endswith((".jpg", ".jpeg", ".png")):
        text = extract_text_from_image(file_bytes)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file_bytes)
    elif filename.endswith(".xlsx"):
        text = extract_text_from_xlsx(file_bytes)
    elif filename.endswith(".csv"):
        text = extract_text_from_csv(file_bytes)
    elif filename.endswith(".txt"):
        text = extract_text_from_txt(file_bytes)
    else:
        return "unknown file"

    # STEP 3: Preprocess extracted text
    if not text:
        return "unknown file"
    text = clean_text(text)
    logging.info(f"Extracted text length: {len(text)}")

    # STEP 4: ML classification, else fallback
    ml_label = classify_with_model(text)

    if ml_label in {"invoice", "bank statement", "driver license"}:
        return ml_label
    else:
        # Fallback keyword check
        if is_bank_statement(text):
            return "bank statement"
        elif is_invoice(text):
            return "invoice"
        elif is_driver_license(text):
            return "driver license"
        else:
            return "unknown file"       