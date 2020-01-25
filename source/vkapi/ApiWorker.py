from threading import Thread

from source.logger.LogWork import LogWork
from source.main.Main import Main
from source.vkapi.AlwaysOnline import AlwaysOnline


class ApiWorker:
    '''
    This class controls threads and script starting behavior
    :return None
    '''

    @staticmethod
    def started() -> None:
        LogWork.log('Script has been started.')
        ApiWorker.thread_controller()

    @staticmethod
    def thread_controller() -> None:
        # Main Messages Handler
        main_messages_handler = Thread(target=Main.handle)
        main_messages_handler.start()

        # Always Online
        AO = Thread(target=AlwaysOnline.online)
        AO.start()
