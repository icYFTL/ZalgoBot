FROM ubuntu:latest
MAINTAINER icYFTL

EXPOSE 8000

CMD [ "nohup python3 ZalgoBot.py &" ]