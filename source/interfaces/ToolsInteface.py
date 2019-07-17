from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class ToolsInterface:
    @staticmethod
    def init(user_id):
        vk = BotAPI()
        vk.message_send('''Выберите инструмент:
                                /GPL - Примерное место жительства человека по его друзьям.''',
                        user_id, JSONWorker.read_json('modules'))
