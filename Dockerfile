FROM python:3.12.2

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /bot

COPY requirements.txt /bot/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /bot/
