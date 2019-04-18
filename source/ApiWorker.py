from Config import Config
from source.Threads import Threads, BotThread
from source.BotApi import BotApi
import hues


class ApiWorker:
    @staticmethod
    def started():
        botapi = BotApi(Config.access_token)
        for admin in Config.admins:
            botapi.message_send('Скрипт начал работу.', admin, False)
        hues.success('Script has been started.')
        thread = Threads()
        thread.start()
        bot_thread = BotThread()
        bot_thread.start()
