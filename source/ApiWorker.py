from Config import Config
from source.BotApi import BotApi
from source.LogWork import LogWork
from source.Threads import Threads


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
        LogWork.add_note('info', 'Script has been started.')
        ApiWorker.thread_controller()
        botapi.message_handler()

    @staticmethod
    def thread_controller():
        LogWork.add_note('info', 'Threads have been started')
        thread = Threads()
        thread.start()
