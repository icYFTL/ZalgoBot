import json
import random

import requests
import vk_api

from Config import Config
from source.other.LogWork import LogWork
from source.other.StaticData import StaticData
# Text handlers
from source.texthandlers.CoutText import CoutTextMaker
from source.texthandlers.FlipTextMaker import FlipTextMaker
from source.texthandlers.ReverseText import ReverseText
from source.texthandlers.ZalgoMaker import ZalgoMaker


class BotAPI:
    '''
    This class controls VK Api requests.
    :param token
    :return message_handler -> [text from message, sender_vk_id]
    :return None
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
                    StaticData.stack_messages.append(
                        {'message': event['object']['text'], 'user_id': event['object']['from_id']})
                    StaticData.new_message_trigger.set()

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
