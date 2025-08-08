FROM python:3.11-slim

# Install Chrome & Chromedriver
RUN apt-get update && apt-get install -y wget unzip curl chromium chromium-driver && \
    rm -rf /var/lib/apt/lists/*

ENV DISPLAY=:99

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:5000 --workers 1 --threads 1 main:app
