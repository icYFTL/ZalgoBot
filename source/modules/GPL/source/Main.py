from source.modules.GPL.Config import Config
from source.modules.GPL.source.DataChecker import DataChecker
from source.modules.GPL.source.DataHandler import DataHandler
from source.modules.GPL.source.InputWorker import InputWorker
from source.modules.GPL.source.LogWork import LogWork


class Main:

    @staticmethod
    def init(user_id=None):
        if DataChecker.check() or not DataChecker.path_checker():
            LogWork.fatal("Bad args")
            exit()
        counter = 1
        LogWork.log("Work started")
        if not user_id:
            user_id = InputWorker.get_user_id()
        for user in user_id:
            LogWork.log('User with ID {} is handling now. ({}/{})'.format(user, str(counter), len(user_id)))
            DH = DataHandler(user_id)
            if Config.module_mod:
                return DH.handler()
            DH.handler()
            counter += 1
