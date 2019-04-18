from threading import Thread
import time

from source.iniWorker import iniWorker
from source.CommandsHandler import CommandsHandler
from source.StaticData import StaticData
from source.BotApi import BotApi
from Config import Config

class Threads(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.botapi = BotApi(Config.access_token)

    def run(self):
        while True:
            if StaticData.stack:
                data = StaticData.stack.pop(0)
                if not iniWorker.user_exists(data[1]):
                    iniWorker.createConfig(data[1])

                if '/' in str(data[0]):
                    CH = CommandsHandler(data[1])
                    CH.identify_comma(data[0])
                    return

                if data[0]:
                    self.botapi.message_send(data[0], data[1], True)
                else:
                    self.botapi.message_send('Гони текст, а не вот это все.', data[1], False)
                time.sleep(0.4)


class BotThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.botapi = BotApi(Config.access_token)

    def run(self):
        while True:
            StaticData.stack.append(self.botapi.message_handler())
