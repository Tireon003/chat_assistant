FROM python:3.12

WORKDIR /app

COPY ../requirements.txt .
COPY ../pyproject.toml .
COPY ../.env .

RUN pip install --no-cache-dir -r requirements.txt

COPY /client ./client

ENV PYTHONPATH=/app