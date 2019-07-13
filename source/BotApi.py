import random

import vk_api
import requests
import json

from Config import Config

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

    def __init__(self):
        self.token = Config.access_token
        self.zalgo = ZalgoMaker()
        self.vk = None
        self.auth()

    def auth(self):
        try:
            self.vk = vk_api.VkApi(token=self.token)
        except Exception:
            print('Bad access token.')
            exit()

    def get_server(self):
        return self.vk.method("groups.getLongPollServer", {'group_id': Config.group_id})

    def message_getter(self):
        while True:
            server = self.get_server()
            data = json.loads(requests.get(
                "{server}?act=a_check&key={key}&ts={ts}&wait=5".format(server=server['server'], key=server['key'],
                                                                       ts=server['ts'])).text)
            for event in data['updates']:
                if event['type'] == 'message_new' and event['object']['out'] == 0:
                    StaticData.stack.append({'message': event['object']['text'], 'user_id': event['object']['from_id']})
                    StaticData.trigger.set()

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
