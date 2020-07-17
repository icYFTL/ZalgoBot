from threading import Thread
from time import sleep

from source.vkapi.BotAPI import BotAPI


class AlwaysOnline(Thread):
    '''
    This class controls online of community.
    '''

    def run(self):
        while True:
            vk = BotAPI()
            vk.enable_online()
            sleep(900)
