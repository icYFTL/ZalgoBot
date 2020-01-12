from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class NothingWaitInterface:
    @staticmethod
    def init(user_id) -> None:
        vk = BotAPI()
        vk.message_send('Ни один из модулей не активен в данный момент.',
                        user_id, JSONWorker.keyboard_handler('default'))
