import logging
import random
from os import _exit

import vk_api

from core import config
# Text handlers
from source.texthandlers import TextHandlers


class BotAPI:
    '''
    This class controls VK Community Api requests.
    '''

    def __init__(self):
        self.token = config['access_token']
        self.vk = None
        self.auth()

    def auth(self) -> None:
        try:
            self.vk = vk_api.VkApi(token=self.token)
        except Exception as e:
            logging.error(str(e))
            logging.fatal('Bad basic VK community access token.')
            _exit(0)

    def message_send(self, message: str, user_id: int, keyboard=None, type_t=None) -> None:
        template = {'user_id': user_id,
                    'random_id': random.randint(0, 999999),
                    'keyboard': keyboard,
                    'message': message}

        if type_t:
            template['message'] = TextHandlers[type_t]().make(message)

        self.vk.method('messages.send', template)

    def enable_online(self) -> None:
        try:
            self.vk.method('groups.enableOnline', {'group_id': config['group_id']})
        except Exception as e:
            logging.warning(str(e))

    def disable_online(self) -> None:
        try:
            self.vk.method('groups.disableOnline', {'group_id': config['group_id']})
        except Exception as e:
            logging.warning(str(e))
