FROM python:3.13-alpine3.21

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /server

COPY requirements.txt .
COPY app app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8443

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8443", "--ssl-certfile=/tls/tls.crt", "--ssl-keyfile=/tls/tls.key", "--log-level", "warning"]
