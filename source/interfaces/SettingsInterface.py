from os import environ

from source.databases.InternalDB import InternalDB
from source.tools.json import *
from source.vkapi.BotAPI import BotAPI
from source.vkapi.UserAPI import UserAPI


class SettingsInterface:

    def __init__(self, user_id) -> None:
        self.user_id = user_id
        self.vk = BotAPI()
        self.IDB = InternalDB()
        self.user = self.IDB.get_user(self.user_id)

    def preview(self):
        if not self.user['token'] or not UserAPI.is_token_valid(self.user['token']):
            token = '⛔'
            self.IDB.update_token(self.user_id, '')
        else:
            token = '✅'
        self.vk.message_send(getMessage('settings_welcome').format(token=token, sub=self.user["subtype"]), self.user_id,
                             getKeyboard('settings'))

    def about(self) -> None:
        from source.static.StaticData import StaticData
        self.vk.message_send(
            getMessage('about_welcome').format(version=StaticData.version),
            self.user_id)

    def access_token(self) -> None:
        self.vk.message_send(
            getMessage('access_token_welcome').format(access_getter_url=environ.get('access_getter_url', 'INVALID')),
            self.user_id, JSONWorker.keyboard_handler('default'))
