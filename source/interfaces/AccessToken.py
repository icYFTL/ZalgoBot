from source.databases.InternalDB import InternalDB
from source.tools.json import *
from source.vkapi.BotAPI import BotAPI
from source.vkapi.UserAPI import UserAPI


class AccessToken:
    @staticmethod
    def check(user_id: int) -> bool:
        vk = BotAPI()
        IDB = InternalDB()
        user = IDB.get_user(user_id)
        if not user['token']:
            vk.message_send(getMessage('no_access_token'),
                            user_id=user_id, keyboard=getKeyboard('settings'))
            IDB.status_changer(user_id=user_id, status=None)
            return False
        elif not UserAPI.is_token_valid(user['token']):
            vk.message_send(getMessage('token_expired'),
                            user_id=user_id, keyboard=getKeyboard('settings'))
            IDB.status_changer(user_id=user_id, status=None)
            return False
        return True
