import time

from source.vkapi.BotAPI import BotAPI


class AlwaysOnline:
    @staticmethod
    def online():
        while True:
            vk = BotAPI()
            vk.enable_online()
            time.sleep(900)
