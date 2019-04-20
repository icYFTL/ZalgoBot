import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

from source.iniWorker import iniWorker
from source.ZalgoMaker import ZalgoMaker
from source.FlipTextMaker import FlipTextMaker
from source.StaticData import StaticData


class BotApi:
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

    def message_send(self, message, user_id):
        self.vk.method("messages.send",
                       {"user_id": user_id,
                        "message": message,
                        'random_id': random.randint(0, 999999)})

    def message_send_zalgo(self, message, user_id):
        data = iniWorker.readConfig(user_id)
        self.vk.method("messages.send",
                       {"user_id": user_id,
                        "message": self.zalgo.zalgo_textarea(message, data[1], data[2]),
                        'random_id': random.randint(0, 999999)})

    def message_send_flip(self, message, user_id):
        self.vk.method("messages.send",
                       {"user_id": user_id,
                        "message": FlipTextMaker.flip(message),
                        'random_id': random.randint(0, 999999)})

    def message_send_reverse(self, message, user_id):
        self.vk.method("messages.send",
                       {"user_id": user_id,
                        "message": message[::-1],
                        'random_id': random.randint(0, 999999)})
