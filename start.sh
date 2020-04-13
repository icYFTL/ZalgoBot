#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

touch zalgo.db
sudo docker cp zalgo:/zalgo.db ./

docker kill gpl_m
docker kill zalgo

docker rm gpl_m
docker rm zalgo

docker image rm gpl_m
docker image rm zalgo

docker build -t gpl ./source/modules/GPL/
docker build -t zalgobot .

docker run -p 7865:7865 -itd --name gpl_m --network="host" gpl
docker run -p 8000:8000 -itd --name zalgo --network="host" zalgobot