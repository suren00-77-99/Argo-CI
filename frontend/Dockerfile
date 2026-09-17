FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Update Debian packages and remove vulnerable package versions
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file first for Docker layer caching
COPY frontend/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY frontend/ .

EXPOSE 5000

CMD ["python", "app.py"]