from io import BytesIO
import pandas as pd

def extract_text_from_csv(file_bytes: bytes) -> str:
    """
    Extracts text content from a CSV file provided as bytes.

    Reads the CSV data from the given bytes, converts it into a pandas DataFrame,
    and returns its string representation without the index column. If an error occurs
    during reading or conversion, logs the error and returns an empty string.

    Args:
        file_bytes (bytes): The CSV file content in bytes.

    Returns:
        str: The string representation of the CSV data without the index, or an empty string on failure.
    """
    try:
        df = pd.read_csv(BytesIO(file_bytes))
        return df.to_string(index=False)
    except Exception as e:
        print(f"[CSV ERROR] {e}")
        return ""