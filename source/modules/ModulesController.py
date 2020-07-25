import json
import logging
from os import path

import requests

from core import config
from source.databases.InternalDB import InternalDB
from source.tools.json import *
from source.vkapi.BotAPI import BotAPI


class ModulesController:
    def __init__(self, user_id, token) -> None:
        self.user_id = user_id
        self.token = token
        self.IDB = InternalDB()
        self.GPL_config_path = path.join(config.get('modules_path', 'source/modules/'), 'GPL', 'config.json')

    def gpl_execute(self, victim_id) -> None:
        g_config = json.load(open('GPL/config.json', 'r'))

        vk = BotAPI()
        vk.message_send(
            getMessage('gpl_work_started', location=self.GPL_config_path),
            user_id=self.user_id, keyboard=getKeyboard('default'))
        self.IDB.status_changer(user_id=self.user_id, status="WFM.gpl.task")
        try:
            vk.message_send(getMessage('gpl_success_done', location=self.GPL_config_path).format(
                data=requests.post(f'http://gpl:{g_config["web_server_port"]}/gpl',
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
