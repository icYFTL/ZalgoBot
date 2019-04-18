import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

from source.iniWorker import iniWorker
from source.ZalgoMaker import ZalgoMaker


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
        longpoll = VkLongPoll(self.vk)

        for event in longpoll.listen():

            if event.type == VkEventType.MESSAGE_NEW:

                if event.to_me:
                    request = event.text
                    return [request, event.user_id]

    def message_send(self, message, user_id, zalgo):

        data = iniWorker.readConfig(user_id)

        if zalgo:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": self.zalgo.zalgo_textarea(message, data[0], data[1]),
                            'random_id': random.randint(0, 999999)})
        else:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": message,
                            'random_id': random.randint(0, 999999)})
