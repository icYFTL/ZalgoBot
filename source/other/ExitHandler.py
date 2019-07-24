import atexit

from Config import Config
from source.databases.InternalBD import InternalBD
from source.logger.LogWork import LogWork
from source.vkapi.BotAPI import BotAPI


class ExitHandler:
    '''
    This script controls actions while exiting.
    :return None
    '''

    @staticmethod
    def register():
        atexit.register(ExitHandler.exit)

    @staticmethod
    def exit():
        try:
            LogWork.warn('Script stop in progress')
            InternalBD.status_cleaner_emergency()
            vk = BotAPI()
            for admin in Config.admins:
                vk.message_send(message='Скрипт был аварийно остановлен.', user_id=admin)
            vk.disable_online()
        except Exception as e:
            LogWork.fatal(str(e))
