from os import path, environ
from threading import Thread

from source.databases.InternalDB import InternalDB
from source.interfaces.AccessToken import AccessToken
from source.modules.ModulesController import ModulesController
from source.tools.json import *
from source.vkapi.BotAPI import BotAPI
from source.vkapi.UserAPI import UserAPI


class GPLInterface:
    def __init__(self, user_id) -> None:
        self.vk = BotAPI()
        self.IDB = InternalDB()
        self.user_id = user_id
        self.user = self.IDB.get_user(user_id)
        self.module_location = path.join(environ['modules_path'], 'GPL')
        self.module_config_location = path.join(self.module_location, 'config.json')

    def preview(self):
        self.vk.message_send(
            getMessage('gpl_description', location=self.module_config_location),
            user_id=self.user_id,
            keyboard=getKeyboard('gpl'))

    def run(self, victim_id, user_id) -> None:
        if not AccessToken.check(user_id):
            return

        if not victim_id:
            self.vk.message_send(getMessage('gpl_give_me_link', location=self.module_config_location),
                                 user_id=user_id)
            self.IDB.status_changer(user_id=user_id, status="GPL_P_G")
            return

        victim_id = UserAPI.get_id_from_url(self.user['token'], victim_id)

        if victim_id == "BadID":
            self.vk.message_send(getMessage('gpl_incorrect_link', location=self.module_config_location),
                                 user_id=user_id, keyboard=JSONWorker.keyboard_handler('gpl'))
            self.IDB.status_changer(user_id=user_id, status=None)
            return

        elif not UserAPI.user_exists(user_id=user_id, token=self.user['token']):
            self.vk.message_send(getMessage('gpl_invalid_account', location=self.module_config_location),
                                 user_id=user_id, keyboard=JSONWorker.keyboard_handler('gpl'))
            self.IDB.status_changer(user_id=user_id, status=None)
            return

        elif UserAPI.user_broken(self.user['token'], victim_id):
            self.vk.message_send(
                getMessage('gpl_closed_account', location=self.module_config_location),
                user_id=user_id, keyboard=JSONWorker.keyboard_handler('gpl'))
            self.IDB.status_changer(user_id=user_id, status=None)
            return

        MC = ModulesController(user_id, self.user['token'])
        thread = Thread(target=MC.gpl_execute, args=(victim_id,))
        thread.start()
