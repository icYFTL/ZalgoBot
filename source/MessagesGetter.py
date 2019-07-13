from threading import Thread
from source.BotApi import BotApi


class MessagesGetter(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.botapi = BotApi()

    def run(self):
        self.botapi.message_getter()
