import time
from threading import Thread

from Config import Config
from source.logger.LogWork import LogWork
from source.main.Main import Main
from source.vkapi.BotAPI import BotAPI


class ApiWorker:
    '''
    This class controls thread and script starting behavior
    :return None
    '''

    @staticmethod
    def started():
        vk = BotAPI()
        for admin in Config.admins:
            vk.message_send(message='Скрипт начал работу.', user_id=admin)
            time.sleep(0.4)
        LogWork.log('Script has been started.')
        ApiWorker.thread_controller()

    @staticmethod
    def thread_controller():
        LogWork.log('Messages handler has been started')

        # Main Messages Handler
        main_messages_handler = Thread(target=Main.handle())

        # Always Online
        vk = BotAPI()
        vk.enable_online()
