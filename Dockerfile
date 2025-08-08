FROM python:3.11-slim

# Install Chrome & dependencies
RUN apt-get update && apt-get install -y wget unzip curl gnupg chromium chromium-driver && rm -rf /var/lib/apt/lists/*

# Set environment variables for Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Start Gunicorn
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5000"]
