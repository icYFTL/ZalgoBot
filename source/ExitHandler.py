from source.BotApi import BotApi
from Config import Config
import hues


class ExitHandler:
    '''
    This script controls actions while exiting.
    :return None
    '''

    @staticmethod
    def exit():
        try:
            BA = BotApi(Config.access_token)
            for admin in Config.admins:
                BA.message_send('Скрипт был аварийно остановлен.', admin, None)
        except Exception as e:
            hues.warn(str(e))

        hues.error('Shutting down...')
