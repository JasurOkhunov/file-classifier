from io import BytesIO
import pandas as pd

def extract_text_from_csv(file_bytes: bytes) -> str:
    try:
        df = pd.read_csv(BytesIO(file_bytes))
        return df.to_string(index=False)
    except Exception as e:
        print(f"[CSV ERROR] {e}")
        return ""