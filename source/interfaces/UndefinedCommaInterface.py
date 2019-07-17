from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class UndefinedCommaInterface:
    @staticmethod
    def init(user_id):
        vk = BotAPI()
        vk.message_send('''Нет такой команды.''',
                        user_id, JSONWorker.read_json('default'))
