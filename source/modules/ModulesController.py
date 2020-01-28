from threading import Thread
import requests
import json

from source.databases.InternalBD import InternalBD
from source.logger.LogWork import LogWork
from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class ModulesController:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

    def gpl_execute(self, victim_id) -> None:
        vk = BotAPI()
        vk.message_send(
            message="Работа модуля GPL начата",
            user_id=self.user_id, keyboard=JSONWorker.keyboard_handler('default'))
        InternalBD.status_changer(user_id=self.user_id, obj="WFM.gpl.task")
        try:
            vk.message_send(message="Успешно завершено.\n{data}".format(
                data=requests.post('http://localhost:7865/gpl',
                                   data=json.dumps({'token': self.token, 'victim_id': victim_id}),
                                   headers={'Content-Type': 'application/json'}).text),
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
            if requests.get('http://localhost:7865/gpl').text == 'ok':
                LogWork.log("GPL ✅")
            else:
                raise BaseException
        except:
            LogWork.error("GPL ⛔")
        try:
            from source.modules.Aurora.source.main.Main import Main
            m_thread = Thread(target=Main.routine)
            m_thread.start()
            LogWork.log("Aurora ✅")
        except:
            LogWork.error("Aurora ⛔")
