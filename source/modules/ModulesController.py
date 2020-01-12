from threading import Thread

from source.databases.InternalBD import InternalBD
from source.logger.LogWork import LogWork
from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class ModulesController:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

    def gpl_execute(self, victim_id) -> None:
        import source.modules.GPL.source.main.Main
        gpl = source.modules.GPL.source.main.Main
        vk = BotAPI()
        vk.message_send(
            message="Работа модуля GPL начата",
            user_id=self.user_id, keyboard=JSONWorker.keyboard_handler('default'))
        InternalBD.status_changer(user_id=self.user_id, obj="WFM.gpl.task")
        try:
            vk.message_send(message="Успешно завершено.\n{data}".format(
                data=gpl.Main.init(token=self.token, user_id=[victim_id])),
                user_id=self.user_id, keyboard=JSONWorker.keyboard_handler('default')
            )
            InternalBD.status_changer(user_id=self.user_id, obj="None")
        except Exception as e:
            LogWork.error(str(e))
            vk.message_send(
                message="Во время работы модуля GPL что-то пошло не так.\nНапишите об этом пожалуйста разработчикам ^^",
                user_id=self.user_id, keyboard=JSONWorker.keyboard_handler('default'))
            InternalBD.status_changer(user_id=self.user_id, obj="None")

    @staticmethod
    def full_time_modules_init() -> None:
        try:
            from source.modules.Aurora.source.main.Main import Main
            m_thread = Thread(target=Main.routine)
            m_thread.start()
            LogWork.log("Aurora ✅")
        except:
            LogWork.error("Aurora ⛔")
