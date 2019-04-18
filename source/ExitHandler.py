from source.BotApi import BotApi
from Config import Config
import hues

class ExitHandler(object):
    def bye():
        try:
            BA = BotApi(Config.access_token)
            for admin in Config.admins:
                BA.message_send('Скрипт был аварийно остановлен.', admin, False)
        except:
            pass

        hues.error('Shutting down...')
