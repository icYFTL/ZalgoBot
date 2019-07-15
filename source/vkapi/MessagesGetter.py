from threading import Thread

from source.vkapi.BotAPI import BotAPI


class MessagesGetter(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.botapi = BotAPI()

    def run(self):
        self.botapi.message_getter()
