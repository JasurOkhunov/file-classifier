# Heron Coding Challenge - File Classifier

## Enhancements Made by Jasur Okhunov

This version of the file classifier improves the original baseline through several real-world, production-ready capabilities including:

### Features & Improvements

#### File Type Support
- **Extended formats:** `.pdf`, `.jpg`, `.jpeg`, `.png`, `.docx`, `.xlsx`, `.csv`, `.txt`
- **OCR for images:** Uses Tesseract for extracting text from image-based documents
- **Office document parsing:** Utilizes `python-docx`, `openpyxl`, and `pandas` for handling Word, Excel, and CSV files

#### Machine Learning Classifier
- **Model:** TF-IDF + Logistic Regression (`scikit-learn`)
- **Trained classes:** `invoice`, `bank statement`, `driver license`
- **Confidence threshold:** Prevents misclassifications
- **Fallback heuristics:** Keyword-based logic for robustness

#### Testing
- **Comprehensive tests:** Edge cases and all supported file types (`tests/`)
- **Test execution:** Via `pytest` locally or inside Docker

#### Docker Support
- **Fully Dockerized:** Includes all dependencies (Tesseract, pdfminer, etc.)
- **Quick start:**
    ```bash
    docker build -t file-classifier .
    docker run -p 5000:5000 file-classifier
    ```

#### Debugging Setup
- **VS Code support:** `launch.json` for step-by-step debugging
- **Easy endpoint testing:** Use `curl` or the frontend UI

#### Frontend UI
- **Simple HTML frontend:** (`frontend/index.html`)
- **File upload & prediction:** Supports all file types
- **Smart API detection:** Switches between local and Render deployments
    ```js
    const API_BASE = location.hostname === "localhost"
        ? "http://localhost:5000"
        : "https://file-classifier.onrender.com";
    ```

---

## Run Instructions

### Local Setup

1. **Clone and set up environment**
    ```bash
    git clone https://github.com/JasurOkhunov/file-classifier.git
    cd file-classifier
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Start backend**
    ```bash
    python -m src.app
    ```
    Or, in VS Code:  
    Press <kbd>F5</kbd> to run the debugger using `launch.json`

3. **Run tests**
    ```bash
    pytest
    ```

4. **Run frontend**
    ```bash
    cd frontend
    python -m http.server 8000
    ```
    Then open your browser to:  
    [http://localhost:8000](http://localhost:8000)

---

### Docker

1. **Build and run**
    ```bash
    docker build -t file-classifier .
    docker run -p 5001:5001 file-classifier
    ```

2. **Test the API**
    ```bash
    curl -X POST -F 'file=@path/to/sample.pdf' http://localhost:5001/classify_file
    ```

---

## Training

- **Training data:**  
  ```
  training_data/
    ├── invoices/
    ├── bank_statements/
    └── driver_licenses/
  ```
- **To retrain the model:**
    ```bash
    python train_model.py
    ```
- **Model output:**  
  `model/document_classifier.joblib`

---

## Deployment Notes (Render)

- **Backend deployed at:**  
  [https://file-classifier.onrender.com](https://file-classifier.onrender.com)
- **OCR step:** Due to resource limitations on Render, OCR processing for image files (e.g., .jpg, .png) may take longer than usual. To prevent premature termination, the timeout has been extended to 30 seconds in the deployed version.
> **Note:** This limitation applies only to the Render deployment. When running locally, OCR processing is fast and operates without delays.

---

## Live Demo (Frontend)

- **Accessible at:**  
  [https://ornate-gumdrop-5f0eca.netlify.app/](https://ornate-gumdrop-5f0eca.netlify.app/)

## CI/CD Pipeline

- **Continuous Integration (CI):**
    - Automated tests (`pytest`) run via GitHub Actions on every push to `main`.
- **Continuous Delivery (CD):**
    - **Frontend (Netlify):** Automatically rebuilds and redeploys the frontend from the `frontend/` folder.
    - **Backend (Render):** Redeploys the Dockerized backend on each push to `main`.