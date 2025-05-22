import joblib
from pathlib import Path

# Load the model
MODEL_PATH = Path("model/document_classifier.joblib")
if not MODEL_PATH.exists():
    raise FileNotFoundError("Trained model not found at model/document_classifier.joblib")

model = joblib.load(MODEL_PATH)

# Get label order
label_names = model.classes_

test_samples = [
    # Invoice examples
    "Invoice Number: INV-123\nAmount Due: $500.00\nCustomer: Acme Corp",
    "Bill To: John Doe\nTotal Due: $99.99\nInvoice Date: 2024-12-01",

    # Bank statement examples
    "Bank of XYZ\nAccount Summary\nEnding Balance: $4,200.00",
    "Statement Period: March\nBalance: $7,300.50\nTransactions Below",

    # Driver's license examples
    "Driver License No: D1234567\nName: John Doe\nDOB: 1990-01-01\nSex: M\nExpires: 2029-01-01",
    "DL#: A9876543\nName: Jane Smith\nDOB: 1985-03-22\nSex: F\nExpiration: 2030-05-15",
    "Issued by: NY DMV\nDLN: Q1234987\nDOB: 1995-10-10\nSex: F\nEXP: 2031-09-15",

    # Edge case
    "Customer Info: Joe\nBalance Due: $100.00\nValid Until: 2030-01-01",

    # Random text
    "This is random text not related to anything."
]

# Run predictions
for i, text in enumerate(test_samples, 1):
    label = model.predict([text])[0]
    probs = model.predict_proba([text])[0]
    confidence = max(probs)
    top_label_index = probs.argmax()

    print(f"\nSample {i}:")
    print("-" * 50)
    print(text)
    print(f"\n Prediction: {label} (Confidence: {confidence:.2f})")
    
    # To show full probability distribution
    print("Probabilities:")
    for j, prob in enumerate(probs):
        print(f"  {label_names[j]}: {prob:.2f}")