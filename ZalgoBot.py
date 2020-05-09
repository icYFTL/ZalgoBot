import logging

logging.basicConfig(filename='zalgo_log.log', level=logging.INFO)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

from source.other.ExitHandler import ExitHandler

# Exit routine
logging.info('Exit routine registered')
ExitHandler.register()

from source.console.Preview import Preview

# Preview
Preview.preview()

# Config2Environ
from os import environ
import json
from copy import copy

data: dict = json.load(open('Config.json', 'r', encoding='UTF-8'))

[data.pop(key) for key in list(data) if 'msg' in key]
data.pop('modules')

environ.update(copy(data))
del data

# Create DB
from source.databases.InternalDB import InternalDB

IDB = InternalDB()
IDB.create()
del IDB

from source.modules.ModulesController import ModulesController

# Full-time work modules
ModulesController.full_time_modules_init()

# Main routine
logging.info('Initialization started')

from source.main.Main import Main
from source.vkapi.AlwaysOnline import AlwaysOnline
from threading import Thread

# Main Messages Handler
main_messages_handler = Thread(target=Main.handle)
main_messages_handler.start()

# Always Online
AO = Thread(target=AlwaysOnline.online)
AO.start()

# Messages GET - Module routine initialization
logging.info('Messages getter started')

from source.vkapi.CallBackAPI import m_thread

m_thread.run(environ.get('web_server_host', 'localhost'), port=int(environ.get("web_server_port", 8000)))
