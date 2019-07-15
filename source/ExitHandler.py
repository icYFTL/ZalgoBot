from Config import Config
from source.LogWork import LogWork
from source.vkapi.BotAPI import BotAPI


class ExitHandler:
    '''
    This script controls actions while exiting.
    :return None
    '''

    @staticmethod
    def exit():
        try:
            BA = BotAPI()
            for admin in Config.admins:
                BA.message_send('Скрипт был аварийно остановлен.', admin, None)
        except Exception as e:
            LogWork.add_note('fatal', str(e))
