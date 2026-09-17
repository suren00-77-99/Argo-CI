FROM python:3.12-slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir --upgrade msgpack

COPY app.py .

RUN chown -R 10001:10001 /app

USER 10001

EXPOSE 8000

CMD ["python", "app.py"]