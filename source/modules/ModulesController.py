from source.databases.InternalBD import InternalBD
from source.other.JSONWorker import JSONWorker
from source.Logger.LogWork import LogWork
from source.vkapi.BotAPI import BotAPI


class ModulesController:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

    def gpl_execute(self, victim_id):
        import source.modules.GPL.GPL
        gpl = source.modules.GPL.GPL.GPL()
        vk = BotAPI()
        vk.message_send(
            message="Работа модуля GPL начата.\nВы можете узнать текущий статус нажав на кнопку /get_status.",
            user_id=self.user_id, keyboard=JSONWorker.read_json('wait'))
        InternalBD.changer(self.user_id, ['status', 'WFM.gpl.task'])
        try:
            vk.message_send(message="Успешно завершено.\n{data}".format(
                data=''.join(gpl.main({'access': self.token, 'user_id': [victim_id]}))),
                user_id=self.user_id, keyboard=JSONWorker.read_json('default')
            )
            InternalBD.changer(self.user_id, ['status', 'None'])
        except Exception as e:
            LogWork.error(str(e))
            vk.message_send(
                message="Во время работы модуля GPL что-то пошло не так.\nНапишите об этом пожалуйста разработчикам ^^",
                user_id=self.user_id, keyboard=JSONWorker.read_json('default'))
            InternalBD.changer(self.user_id, ['status', 'None'])

    def aurora_execute(self, user_id):
        pass
