import os

from source.logger.LogWork import LogWork
from source.other.ExitHandler import ExitHandler

# Exit routine
LogWork.log('Exit routine registered')
ExitHandler.register()

from source.console.Preview import Preview

# Preview
Preview.preview()

from source.modules.ModulesController import ModulesController

# Full-time work modules
ModulesController.full_time_modules_init()

# Main routine
LogWork.log('Initialization started.')

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
LogWork.log('Messages getter has been started')

from source.vkapi.CallBackAPI import m_thread

m_thread.run('localhost', port=int(os.environ.get("PORT", 8000)))
