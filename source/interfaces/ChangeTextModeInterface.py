from source.databases.InternalDB import InternalDB
from source.tools.json import *
from source.vkapi.BotAPI import BotAPI


class ChangeTextModeInterface:
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id
        self.vk = BotAPI()
        self.IDB = InternalDB()

    def preview(self) -> None:
        self.vk.message_send(getMessage('current_mode').format(mode=self.IDB.get_user(self.user_id)["current_mode"]),
                             self.user_id, getKeyboard('4way'))

    def change(self, mode: str) -> None:
        self.IDB.mode_changer(user_id=self.user_id, mode=mode)
        self.vk.message_send(getMessage('mode_activated').format(mode[0].upper() + ''.join(mode[1:])).replace('_', ' '),
                             self.user_id, getKeyboard('4way'.format(mode)))
