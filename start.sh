#!/bin/bash

docker build -t gpl ./source/modules/GPL/
docker build -t zalgobot .

docker run -p 7865:7865 -itd gpl
docker run -p 8000:8000 -itd zalgobot