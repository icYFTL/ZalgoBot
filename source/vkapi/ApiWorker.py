import time

from Config import Config
from source.other.LogWork import LogWork
from source.vkapi.BotAPI import BotAPI
from source.vkapi.MessagesGetter import MessagesGetter
from source.vkapi.MessagesHandler import MessagesHandler


class ApiWorker:
    '''
    This class controls thread and script starting behavior
    :return None
    '''

    @staticmethod
    def started():
        botapi = BotAPI()
        for admin in Config.admins:
            botapi.message_send(message='Скрипт начал работу.', user_id=admin)
            time.sleep(0.4)
        LogWork.log('Script has been started.')
        ApiWorker.thread_controller()

    @staticmethod
    def thread_controller():
        LogWork.log('Messages handling has been started')

        MG = MessagesGetter()
        MG.start()

        MH = MessagesHandler()
        MH.start()
