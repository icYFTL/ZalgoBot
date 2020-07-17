#!/bin/bash

docker network inspect zalgo_bridge
if [$? != 0]
  docker network create --driver=bridge zalgo_bridge

