import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

from Config import Config
from source.ZalgoMaker import ZalgoMaker


class ApiWorker:
    def __init__(self):
        self.token = Config.access_token
        self.vk = None
        self.zalgo = ZalgoMaker()
        self.auth()
        self.started()

    def started(self):
        for admin in Config.admins:
            self.message_send('Скрипт начал работу.', admin, False)

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
        if zalgo:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": self.zalgo.zalgo_textarea(message, '3', ['up', 'mid', 'down']),
                            'random_id': random.randint(0, 999999)})
        else:
            self.vk.method("messages.send",
                           {"user_id": user_id,
                            "message": message,
                            'random_id': random.randint(0, 999999)})

    def get_message(self):
        data = self.message_handler()
        self.message_send(data[0], data[1], True)
