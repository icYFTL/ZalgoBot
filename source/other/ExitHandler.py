import atexit
import logging

from core import config
from source.databases.InternalDB import InternalDB
from source.tools.json import getMessage
from source.vkapi.BotAPI import BotAPI


class ExitHandler:
    '''
    This script controls actions while exiting.
    :return None
    '''

    @staticmethod
    def register() -> None:
        atexit.register(ExitHandler.exit)

    @staticmethod
    def exit() -> None:
        try:
            logging.warning('Script stopping in progress...')

            IDB = InternalDB()
            IDB.status_cleaner_emergency()

            vk = BotAPI()
            for admin in config.get('admins', []).split(','):
                vk.message_send(getMessage('script_stopped'), user_id=admin)

            vk.disable_online()
        except Exception as e:
            logging.fatal(str(e))
