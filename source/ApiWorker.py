from Config import Config
from source.BotApi import BotApi
from source.LogWork import LogWork
from source.MessagesHandler import MessagesHandler
from source.MessagesGetter import MessagesGetter


class ApiWorker:
    '''
    This class controls thread and script starting behavior
    :return None
    '''

    @staticmethod
    def started():
        botapi = BotApi()
        for admin in Config.admins:
            botapi.message_send('Скрипт начал работу.', admin, None)
        LogWork.add_note('info', 'Script has been started.')
        ApiWorker.thread_controller()

    @staticmethod
    def thread_controller():
        LogWork.add_note('info', 'Handling has been started')

        MG = MessagesGetter()
        MG.start()

        MH = MessagesHandler()
        MH.start()
