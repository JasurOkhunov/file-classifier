import re
import joblib
from pathlib import Path

MODEL_PATH = Path("model/document_classifier.joblib") # Load trained ML model
print("MODEL_PATH: ", MODEL_PATH)
ml_model = joblib.load(MODEL_PATH)

def classify_with_model(text: str, threshold: float = 0.6, debug: bool = True) -> str:
    probs = ml_model.predict_proba([text])[0]
    label = ml_model.predict([text])[0]
    confidence = max(probs)

    if debug:
        print(f"[ML] Prediction: {label} | Confidence: {confidence:.2f}", flush=True)

    return label if confidence >= threshold else "unknown file"

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def is_bank_statement(text):
    return any(kw in text for kw in [
        "bank", "account summary", "bank of", "statement period", "ending balance"
    ])

def is_invoice(text):
    return any(kw in text for kw in [
        "invoice", "total due", "invoice number", "bill to", "amount payable"
    ])

def is_driver_license(text):
    keywords = [
        "driver",
        "license",
        "issued",
        "class",
        "state",
        "hair",
        "eyes",
        "date of birth", "dob",
        "expires", "exp",
        "sex", "gender"
    ]
    score = sum(kw in text for kw in keywords)
    return score >= 4

