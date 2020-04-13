import time

from source.vkapi.BotAPI import BotAPI


class AlwaysOnline:
    '''
    This class controls online of community.
    '''

    @staticmethod
    def online() -> None:
        while True:
            vk = BotAPI()
            vk.enable_online()
            time.sleep(900)
