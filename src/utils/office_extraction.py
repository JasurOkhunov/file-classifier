from docx import Document
import openpyxl
from io import BytesIO

def extract_text_from_docx(file_bytes: bytes) -> str:
    """
    Extracts and returns the text content from a DOCX file provided as bytes.

    Args:
        file_bytes (bytes): The binary content of the DOCX file.

    Returns:
        str: The extracted text from the document, with paragraphs separated by newlines.
             Returns an empty string if extraction fails.

    Exceptions:
        Prints an error message and returns an empty string if an exception occurs during extraction.
    """
    try:
        doc = Document(BytesIO(file_bytes))
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    except Exception as e:
        print(f"[DOCX ERROR] {e}")
        return ""

def extract_text_from_xlsx(file_bytes: bytes) -> str:
    """
    Extracts and concatenates all text content from an XLSX file provided as bytes.

    Args:
        file_bytes (bytes): The XLSX file content in bytes.

    Returns:
        str: A string containing all non-empty cell values from all sheets, separated by newlines.
        
    Exceptions:
        Prints an error message and returns an empty string if extraction fails.
    """
    try:
        wb = openpyxl.load_workbook(filename=BytesIO(file_bytes), data_only=True)
        text = []
        for sheet in wb.worksheets:
            for row in sheet.iter_rows(values_only=True):
                for cell in row:
                    if cell:
                        text.append(str(cell))
        return "\n".join(text)
    except Exception as e:
        print(f"[XLSX ERROR] {e}")
        return ""



