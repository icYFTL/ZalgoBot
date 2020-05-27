FROM python:3.7-alpine as zalgobot
EXPOSE 8000
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY source/ /app
COPY ZalgoBot.py /app
COPY zalgo.db /app
COPY Config.json /app

