# Use a minimal Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies needed by Tesseract, pdfminer, and Pillow
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask will run on
EXPOSE 5000

# Start the Flask server
CMD ["python", "-m", "src.app"]