from source.tools.json import *
from source.vkapi.BotAPI import BotAPI


class ToolsInterface:
    def __init__(self, user_id) -> None:
        self.vk = BotAPI()
        self.user_id = user_id

    def preview(self):
        self.vk.message_send(getMessage('tools_welcome'),
                             self.user_id, JSONWorker.keyboard_handler('modules'))
