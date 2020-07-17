import json
import logging
from os import environ, path

import requests

from source.databases.InternalDB import InternalDB
from source.tools.json import *
from source.vkapi.BotAPI import BotAPI


class ModulesController:
    def __init__(self, user_id, token) -> None:
        self.user_id = user_id
        self.token = token
        self.IDB = InternalDB()
        self.GPL_config_path = path.join(environ['modules_path'], 'GPL', 'config.json')

    def gpl_execute(self, victim_id) -> None:
        vk = BotAPI()
        vk.message_send(
            getMessage('gpl_work_started', location=self.GPL_config_path),
            user_id=self.user_id, keyboard=getKeyboard('default'))
        self.IDB.status_changer(user_id=self.user_id, status="WFM.gpl.task")
        try:
            vk.message_send(getMessage('gpl_success_done', location=self.GPL_config_path).format(
                data=requests.post('http://localhost:7865/gpl',
                                   data=json.dumps({'token': self.token, 'victim_id': victim_id}),
                                   headers={'Content-Type': 'application/json'}).text),
                user_id=self.user_id, keyboard=getKeyboard('default')
            )
            self.IDB.status_changer(user_id=self.user_id, status=None)
        except Exception as e:
            logging.error(str(e))
            vk.message_send(
                getMessage('gpl_exception', location=self.GPL_config_path),
                user_id=self.user_id, keyboard=getKeyboard('default'))
            self.IDB.status_changer(user_id=self.user_id, status=None)

    @staticmethod
    def full_time_modules_init() -> None:
        try:
            if requests.get('http://localhost:7865/gpl').text == 'ok':
                logging.info("[RUNNING] GPL ✅")
            else:
                raise BaseException
        except Exception as e:
            logging.error("[RUNNING] GPL ⛔")
            logging.error(str(e))
        # try:
        #     raise NotImplementedError
        #     from source.modules.Aurora.source.main.Main import Main
        #     m_thread = Thread(target=Main.routine)
        #     m_thread.start()
        #     logging.error("Aurora ✅")
        # except Exception as e:
        #     logging.error("Aurora ⛔")
        #     logging.error(str(e))
