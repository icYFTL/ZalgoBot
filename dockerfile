FROM python:3.7-alpine as zalgobot
EXPOSE 8000
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY source/ /source
COPY ZalgoBot.py /ZalgoBot.py
COPY Config.py /Config.py

WORKDIR /
CMD ["nohup", "python3", "ZalgoBot.py", "&"]