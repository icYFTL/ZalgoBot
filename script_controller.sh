#!/bin/bash
sleep 10800
pkill -f ZalgoBot
sleep 5
$(nohup python3 ./ZalgoBot.py &)
exit 1