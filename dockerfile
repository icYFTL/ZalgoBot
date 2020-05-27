FROM python:3.7-alpine as zalgobot
EXPOSE 8000
RUN mkdir /zalgo
WORKDIR /zalgo
COPY requirements.txt .
COPY source/ .
COPY ZalgoBot.py .
COPY zalgo.db .
COPY Config.json .

RUN pip3 install -r requirements.txt


