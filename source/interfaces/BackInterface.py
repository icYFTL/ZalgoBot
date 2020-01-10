from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class BackInterface:
    @staticmethod
    def init(user_id) -> None:
        vk = BotAPI()
        vk.message_send('Отменено', user_id, JSONWorker.read_json('default'))
