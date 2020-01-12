from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class ToolsInterface:
    @staticmethod
    def init(user_id) -> None:
        vk = BotAPI()
        vk.message_send('''Выберите инструмент:
GPL - Примерное место жительства человека по его друзьям.
Aurora - Автоматическое удаление друзей, удаливших вас, из подписок.''',
                        user_id, JSONWorker.keyboard_handler('modules'))
