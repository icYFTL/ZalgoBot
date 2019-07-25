from multiprocessing import Process

from source.modules.Aurora.source.logger.LogWork import LogWork
from source.modules.Aurora.source.main.Main import Main


class ThreadsController:
    @staticmethod
    def init_main_routine():
        main = Process(target=Main.routine)
        main.start()
        LogWork.log("Main routine thread has been started")
