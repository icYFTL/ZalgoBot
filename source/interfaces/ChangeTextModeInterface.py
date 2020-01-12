from source.databases.InternalBD import InternalBD
from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class ChangeTextModeInterface:
    @staticmethod
    def init(user_id) -> None:
        vk = BotAPI()
        vk.message_send('Выберите режим:',
                        user_id, JSONWorker.keyboard_handler('4way'))

    @staticmethod
    def change(user_id, mode) -> None:
        vk = BotAPI()
        InternalBD.mode_changer(user_id=user_id, obj=mode)
        vk.message_send('Режим {} активирован.'.format(mode[0].upper() + ''.join(mode[1:])),
                        user_id, JSONWorker.keyboard_handler('4way'.format(mode)))
