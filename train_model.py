import joblib
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from src.utils.office_extraction import (
    extract_text_from_docx,
    extract_text_from_xlsx
)
from src.utils.csv_extraction import extract_text_from_csv
from src.utils.txt_extraction import extract_text_from_txt
from src.utils.pdf_extraction import extract_text_from_pdf
from src.utils.ocr import extract_text_from_image

# Root path of training data
TRAIN_DIR = Path("training_data")

# Load text based on file extension
def extract_text_by_type(filepath: Path) -> str:
    ext = filepath.suffix.lower()
    try:
        with open(filepath, "rb") as f:
            file_bytes = f.read()
        if ext == ".pdf":
            return extract_text_from_pdf(file_bytes)
        elif ext in (".jpg", ".jpeg", ".png"):
            return extract_text_from_image(file_bytes)
        elif ext == ".docx":
            return extract_text_from_docx(file_bytes)
        elif ext == ".xlsx":
            return extract_text_from_xlsx(file_bytes)
        elif ext == ".csv":
            return extract_text_from_csv(file_bytes)
        elif ext == ".txt":
            return extract_text_from_txt(file_bytes)
    except Exception as e:
        print(f"[ERROR] {filepath.name}: {e}")
    return ""

# Collect data
X, y = [], []

for label_dir in TRAIN_DIR.iterdir():
    if label_dir.is_dir():
        label = label_dir.name
        label = label_dir.name.rstrip("s")
        for file_path in label_dir.glob("*"):
            text = extract_text_by_type(file_path)
            if text:
                X.append(text)
                y.append(label)

print(f"Loaded {len(X)} samples from {TRAIN_DIR}")

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Define model pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

# Train
model.fit(X_train, y_train)
print("Model trained.")

# Evaluate
y_pred = model.predict(X_test)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
Path("model").mkdir(exist_ok=True)
joblib.dump(model, "model/document_classifier.joblib")
print("Model saved to model/document_classifier.joblib")