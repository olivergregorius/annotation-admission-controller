FROM python:3.13-alpine3.21

WORKDIR /app

COPY requirements.txt /app
COPY app /app/app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8443

CMD ["fastapi", "run", "app/main.py"]
