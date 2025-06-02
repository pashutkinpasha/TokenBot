FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install pyTelegramBotAPI

CMD ["python", "main.py"]
