import random

import vk_api

from source.modules.Aurora.Config import Config
from source.modules.Aurora.source.logger.LogWork import LogWork


class BotAPI:
    def __init__(self):
        self.token = Config.vk_community_token
        self.vk = None
        self.auth()

    def auth(self):
        try:
            self.vk = vk_api.VkApi(token=self.token)
        except:
            LogWork.fatal('Bad community access token.')

    def message_send(self, message, user_id):
        self.vk.method("messages.send",
                       {'message': message, 'user_id': user_id, 'random_id': random.randint(0, 1000000)})
