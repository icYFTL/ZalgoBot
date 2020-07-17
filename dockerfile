FROM python:3 as zalgobot
EXPOSE 8000

RUN mkdir /opt/app
WORKDIR /opt/app

COPY requirements.txt .
COPY source/ ./source/
COPY ZalgoBot.py .
COPY zalgo.db .
COPY config.json .

RUN pip3 install -r requirements.txt


