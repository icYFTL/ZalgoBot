from source.BotApi import BotApi
from Config import Config
import hues


class ExitHandler:
    @staticmethod
    def bye():
        try:
            BA = BotApi(Config.access_token)
            for admin in Config.admins:
                BA.message_send('Скрипт был аварийно остановлен.', admin, None)
        except:
            pass

        hues.error('Shutting down...')
