FROM python:3.12-slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m pip uninstall -y msgpack setuptools || true \
    && python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir --no-compile \
       "setuptools>=78.1.1" \
       "msgpack>=1.2.1" \
    && python -m pip install --no-cache-dir --no-compile -r requirements.txt \
    && python -m pip install --no-cache-dir --no-compile --upgrade \
       "setuptools>=78.1.1" \
       "msgpack>=1.2.1"

COPY app.py .

RUN chown -R 10001:10001 /app

USER 10001

EXPOSE 8080

CMD ["python", "app.py"]