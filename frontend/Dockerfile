FROM python:3.12-slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Update operating-system packages
RUN python -m pip uninstall -y msgpack setuptools || true \
    && find /usr/local/lib/python3.12/site-packages \
       -maxdepth 1 \
       \( -iname 'msgpack*' -o -iname 'setuptools*' \) \
       -exec rm -rf {} +

# Install clean, fixed versions
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir --no-compile \
       "msgpack==1.2.2" \
       "setuptools==84.0.0" \
    && python -m pip install --no-cache-dir --no-compile -r requirements.txt

COPY app.py .

RUN chown -R 10001:10001 /app

USER 10001

EXPOSE 8000

CMD ["python", "app.py"]