FROM python:3.11-slim-bookworm

WORKDIR /app

ENV PYTHONPATH=/app/backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install --with-deps

# Install Tesseract OCR and its language data
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]