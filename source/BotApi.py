import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from source.BDWorker import BDWorker
from source.StaticData import StaticData
from source.texthandlers.CoutText import CoutTextMaker
from source.texthandlers.FlipTextMaker import FlipTextMaker
from source.texthandlers.ZalgoMaker import ZalgoMaker


class BotApi:
    '''
    This class controls VK Api requests.
    :param token
    :return message_handler -> [text from message, sender_vk_id]
    :return None
    '''

    def __init__(self, token):
        self.token = token
        self.zalgo = ZalgoMaker()
        self.vk = None
        self.auth()

    def auth(self):
        try:
            self.vk = vk_api.VkApi(token=self.token)
        except Exception:
            print('Bad access token.')
            exit()

    def message_handler(self):
        while True:
            longpoll = VkLongPoll(self.vk)

            for event in longpoll.listen():

                if event.type == VkEventType.MESSAGE_NEW:

                    if event.to_me:
                        request = event.text
                        StaticData.stack.append([request, event.user_id])

    def message_send(self, message, user_id, keyboard):
        if keyboard:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": message,
                            'random_id': random.randint(0, 999999),
                            'keyboard': keyboard
                            })
        else:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": message,
                            'random_id': random.randint(0, 999999),
                            })

    def message_send_zalgo(self, message, user_id, keyboard):
        data = BDWorker.getter(user_id)
        if keyboard:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": self.zalgo.zalgo_textarea(message, data.get('zalgo_type')),
                            'random_id': random.randint(0, 999999),
                            'keyboard': keyboard
                            })
        else:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": self.zalgo.zalgo_textarea(message, data.get('zalgo_type')),
                            'random_id': random.randint(0, 999999),
                            })

    def message_send_flip(self, message, user_id, keyboard):
        if keyboard:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": FlipTextMaker.flip(message),
                            'random_id': random.randint(0, 999999),
                            'keyboard': keyboard
                            })
        else:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": FlipTextMaker.flip(message),
                            'random_id': random.randint(0, 999999),
                            })

    def message_send_reverse(self, message, user_id, keyboard):
        if keyboard:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": message[::-1],
                            'random_id': random.randint(0, 999999),
                            'keyboard': keyboard
                            })
        else:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": message[::-1],
                            'random_id': random.randint(0, 999999)})

    def message_send_cout(self, message, user_id, keyboard):
        if keyboard:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": CoutTextMaker.cout(message),
                            'random_id': random.randint(0, 999999),
                            'keyboard': keyboard
                            })
        else:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": CoutTextMaker.cout(message),
                            'random_id': random.randint(0, 999999)})
