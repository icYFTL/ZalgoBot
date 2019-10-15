from source.modules.GPL.Config import Config
from source.modules.GPL.source.data_workers.DataChecker import DataChecker
from source.modules.GPL.source.data_workers.DataHandler import DataHandler
from source.modules.GPL.source.data_workers.InputWorker import InputWorker
from source.modules.GPL.source.logger.LogWork import LogWork


class Main:

    @staticmethod
    def init(user_id=None, token=None):
        if token:
            Config.user_vk_access_token = token
        if DataChecker.check() or not DataChecker.path_checker():
            LogWork.fatal('Bad args or path creating trouble')
            raise BaseException
        counter = 1
        LogWork.log('Work started')
        if not user_id:
            user_id = InputWorker.get_user_id()

        for user in user_id:
            if not user:
                LogWork.fatal("Bad ID")
                raise BaseException
            LogWork.log(f'User with ID {user} is handling now. ({counter}/{len(user_id)})')
            DH = DataHandler(user)
            return DH.handler()
