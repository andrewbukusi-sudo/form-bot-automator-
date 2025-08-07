FROM python:3.11-slim

# Install Chromium and dependencies
RUN apt-get update && apt-get install -y \
    chromium chromium-driver wget unzip curl gnupg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="/usr/local/bin/chromedriver:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . /app
WORKDIR /app

# Expose port and define entrypoint
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]