FROM python:3.7-alpine as zalgobot
EXPOSE 8000
RUN mkdir /zalgo
WORKDIR /zalgo
COPY requirements.txt /zalgo
COPY source/ /zalgo
COPY ZalgoBot.py /zalgo
COPY zalgo.db /zalgo
COPY Config.json /zalgo

RUN pip3 install -r requirements.txt


