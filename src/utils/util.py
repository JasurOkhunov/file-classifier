import re
import joblib
from pathlib import Path

MODEL_PATH = Path("model/document_classifier.joblib") # Load trained ML model
print("MODEL_PATH: ", MODEL_PATH)
ml_model = joblib.load(MODEL_PATH)

def classify_with_model(text: str, threshold: float = 0.6, debug: bool = True) -> str:
    """
    Classifies the given text using a pre-trained machine learning model and returns the predicted label
    if the model's confidence exceeds the specified threshold.

    Args:
        text (str): The input text to classify.
        threshold (float, optional): The minimum confidence required to accept the prediction. Defaults to 0.6.
        debug (bool, optional): If True, prints the prediction and confidence for debugging purposes. Defaults to True.

    Returns:
        str: The predicted label if confidence is above the threshold; otherwise, "unknown file".
    """
    probs = ml_model.predict_proba([text])[0]
    label = ml_model.predict([text])[0]
    confidence = max(probs)

    if debug:
        print(f"[ML] Prediction: {label} | Confidence: {confidence:.2f}", flush=True)

    return label if confidence >= threshold else "unknown file"

def clean_text(text):
    """
    Cleans and normalizes a given text string by converting it to lowercase,
    replacing multiple whitespace characters with a single space, and trimming
    leading and trailing whitespace.

    Args:
        text (str): The input text string to be cleaned.

    Returns:
        str: The cleaned and normalized text string.
    """
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def is_bank_statement(text):
    """
    Determines if the given text is likely to be a bank statement.

    Checks for the presence of common bank statement keywords such as
    "bank", "account summary", "bank of", "statement period", or "ending balance".

    Args:
        text (str): The text to be analyzed.

    Returns:
        bool: True if any bank statement keyword is found in the text, False otherwise.
    """
    return any(kw in text for kw in [
        "bank", "account summary", "bank of", "statement period", "ending balance"
    ])

def is_invoice(text):
    """
    Checks if the given text contains keywords commonly found in invoices.

    Args:
        text (str): The text to be checked for invoice-related keywords.

    Returns:
        bool: True if any invoice-related keyword is found in the text, False otherwise.
    """
    return any(kw in text for kw in [
        "invoice", "total due", "invoice number", "bill to", "amount payable"
    ])

def is_driver_license(text):
    """
    Determines if the given text likely refers to a driver's license by checking for the presence of specific keywords.

    Args:
        text (str): The text to be analyzed.

    Returns:
        bool: True if at least 4 keywords related to driver's licenses are found in the text, False otherwise.
    """
    keywords = [
        "driver", "license", "issued", "class", "state", "hair", "eyes",
        "date of birth", "dob", "expires", "exp", "sex", "gender"
    ]
    score = sum(kw in text for kw in keywords)
    return score >= 4

