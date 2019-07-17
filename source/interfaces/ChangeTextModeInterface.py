from source.databases.InternalBD import InternalBD
from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class ChangeTextModeInterface:
    @staticmethod
    def init(user_id):
        vk = BotAPI()
        vk.message_send('''Выберите режим:
            /zalgo - Включить режим Zalgo
            /flip - Включить режим Flip
            /reverse - Включить режим Reverse
            /cout - Включить режим Crossed Out''',
                        user_id, JSONWorker.read_json('4way'))

    @staticmethod
    def change(user_id, mode):
        vk = BotAPI()
        InternalBD.changer(user_id, ['current_mode', mode])
        vk.message_send('Режим {} активирован.'.format(mode[0].upper() + ''.join(mode[1:])),
                        user_id, JSONWorker.read_json('4way'.format(mode)))
