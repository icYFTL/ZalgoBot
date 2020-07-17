from core import *

from source.other.ExitHandler import ExitHandler

# Exit routine
logging.info('Exit routine registered')
ExitHandler.register()

# Create DB TODO: Probably bad way. REFACTOR
from source.databases.InternalDB import InternalDB

InternalDB().create()

from source.modules.ModulesController import ModulesController

# Full-time work modules
ModulesController.full_time_modules_init()

# Main routine
logging.info('Initialization started')

from source.main.Main import Main
from source.vkapi.AlwaysOnline import AlwaysOnline

# Main Messages Handler
Main().start()

# Always Online
AlwaysOnline().start()

# Messages GET - Module routine initialization
logging.info('Messages getter started')

from source.vkapi.CallBackAPI import m_thread

m_thread.run(config.get('web_server_host', 'localhost'), port=int(config.get("web_server_port", 8000)))
