FROM python:3.12-slim

WORKDIR /app

# Update Debian packages to patched versions
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app.py .

EXPOSE 8000

CMD ["python", "app.py"]