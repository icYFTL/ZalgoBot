from Config import Config
from source.Threads import Threads
from source.BotApi import BotApi
import hues


class ApiWorker:
    '''
    This class controls thread and script starting behavior
    :return None
    '''

    @staticmethod
    def started():
        botapi = BotApi(Config.access_token)
        for admin in Config.admins:
            botapi.message_send('Скрипт начал работу.', admin, None)
        hues.success('Script has been started.')
        ApiWorker.thread_controller()
        botapi.message_handler()

    @staticmethod
    def thread_controller():
        thread = Threads()
        thread.start()
