import random
import os
import vk_api

from Config import Config
from source.logger.LogWork import LogWork
# Text handlers
from source.texthandlers.CoutText import CoutTextMaker
from source.texthandlers.FlipTextMaker import FlipTextMaker
from source.texthandlers.ReverseText import ReverseText
from source.texthandlers.ZalgoMaker import ZalgoMaker


class BotAPI:
    '''
    This class controls VK Community Api requests.
    '''

    def __init__(self):
        self.token = Config.access_token
        self.vk = None
        self.auth()

    def auth(self):
        try:
            self.vk = vk_api.VkApi(token=self.token)
        except:
            LogWork.fatal('Bad basic access token.')
            os._exit(0)

    def message_send(self, message, user_id, keyboard=None, type_t=None):
        template = {"user_id": user_id,
                    'random_id': random.randint(0, 999999),
                    'keyboard': keyboard}
        if not type_t:
            template.update({"message": message})
        elif type_t == 'zalgo':
            template.update({"message": ZalgoMaker.zalgo_textarea(message)})
        elif type_t == 'flip':
            template.update({"message": FlipTextMaker.flip(message)})
        elif type_t == 'reverse':
            template.update({"message": ReverseText.reverse(message)})
        elif type_t == 'cout':
            template.update({"message": CoutTextMaker.cout(message)})
        self.vk.method('messages.send', template)

    def enable_online(self):
        try:
            self.vk.method("groups.enableOnline", {'group_id': Config.group_id})
        except:
            pass

    def disable_online(self):
        try:
            self.vk.method("groups.disableOnline", {'group_id': Config.group_id})
        except:
            pass
