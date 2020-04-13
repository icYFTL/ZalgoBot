from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class ServiceInterface:
    @staticmethod
    def start(user_id) -> None:
        vk = BotAPI()
        vk.message_send('''Добро пожаловать в ZalgoBot.
    ZalgoBot умеет работать с текстом, а еще он умеет делать разные штуки.

    Также, у нас есть настройки в которые неплохо было бы заглянуть.
            ''', user_id, JSONWorker.keyboard_handler('default'))

    @staticmethod
    def back(user_id) -> None:
        vk = BotAPI()
        vk.message_send('Отменено', user_id, JSONWorker.keyboard_handler('default'))

    @staticmethod
    def undefined(user_id) -> None:
        vk = BotAPI()
        vk.message_send('Нет такой команды.',
                        user_id)
