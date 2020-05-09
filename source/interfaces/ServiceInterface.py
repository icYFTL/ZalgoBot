from source.tools.json import *
from source.vkapi.BotAPI import BotAPI


class ServiceInterface:
    __vk = BotAPI()

    @staticmethod
    def start(user_id: int) -> None:
        ServiceInterface.__vk.message_send(getMessage('welcome'), user_id, getKeyboard('default'))

    @staticmethod
    def back(user_id: int) -> None:
        ServiceInterface.__vk.message_send(getMessage('canceled'), user_id, getKeyboard('default'))

    @staticmethod
    def undefined(user_id: int) -> None:
        ServiceInterface.__vk.message_send(getMessage('undefined_comma'), user_id)
