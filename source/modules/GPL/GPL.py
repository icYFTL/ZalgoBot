import json
import os

from source.main.Server import gpl

data: dict = json.load(open('Config.json', 'r', encoding='UTF-8'))

gpl.run(data['web_server_host'], port=int(os.environ.get("PORT", data['web_server_port'])))
