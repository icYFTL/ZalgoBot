#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit
fi

if ! [ -f ./ZalgoBot.py ]; then
  echo "Please run in ZalgoBot's root directory"
  exit
fi

if command -v python3 --version > /dev/null 2>&1; then
  echo "Python ✅"
else
  echo "Python 🚫"
  echo "Python3 isn't installed"
  exit
fi

pwd | python3 -c "import sys, json;
data = json.load(open('Config.json', 'r', encoding='UTF-8'))
data['absolute_path'] = sys.stdin.read().replace('\n', '')
open('Config.json', 'w', encoding='UTF-8').write(json.dumps(data,ensure_ascii=False))"

touch zalgo.db # Important

python3 ./deploy/Destroy.py
python3 ./deploy/Update.py
python3 ./deploy/ModulesPrepare.py
python3 ./deploy/Deploy.py
