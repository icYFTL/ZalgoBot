from Config import Config
from source.BotApi import BotApi
from source.LogWork import LogWork


class ExitHandler:
    '''
    This script controls actions while exiting.
    :return None
    '''

    @staticmethod
    def exit():
        try:
            BA = BotApi()
            for admin in Config.admins:
                BA.message_send('Скрипт был аварийно остановлен.', admin, None)
        except Exception as e:
            LogWork.add_note('fatal', str(e))
