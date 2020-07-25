#!/bin/bash

if [ "$EUID" -ne 0 ]; then # Is started with root rights
  echo "Please run as root"
  exit
fi

if ! [ -f ./ZalgoBot.py ]; then # Is started from root dir
  echo "Please run in ZalgoBot's root directory"
  exit
fi

if command -v python3 --version >/dev/null 2>&1; then # Check is python3 installed
  echo "Python ✅"
else
  echo "Python 🚫"
  echo "Python3 isn't installed"
  exit
fi

pwd | python3 -c "import sys, json;
data = json.load(open('config.json', 'r', encoding='UTF-8'))
data['absolute_path'] = sys.stdin.read().replace('\n', '')
open('config.json', 'w', encoding='UTF-8').write(json.dumps(data,ensure_ascii=False))" # Save absolute path to config.json

touch zalgo.db # Important

python3 ./deploy/Update.py
python3 ./deploy/ModulesPrepare.py
python3 ./deploy/Deploy.py
