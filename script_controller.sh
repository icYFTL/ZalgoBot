#!/bin/bash
sleep 86400
Get_PID="$(sudo ps -fA | grep 'python3 ZalgoBot.py')"
read -ra ADDR <<< "$Get_PID"
$(sudo kill ${ADDR[1]})
sleep 5
$(nohup python3 ./ZalgoBot.py &)
exit 1