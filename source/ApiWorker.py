from Config import Config
from source.Threads import Threads
from source.BotApi import BotApi
from source.StaticData import StaticData
import hues


class ApiWorker:
    def __init__(self):
        self.token = Config.access_token
        self.botapi = BotApi(self.token)
        self.started()

    def started(self):
        for admin in Config.admins:
            self.botapi.message_send('Скрипт начал работу.', admin, False)
        hues.success('Script has been started.')
        Thread = Threads(self.botapi)
        Thread.start()

    def get_message(self):
        while True:
            data = self.botapi.message_handler()
            StaticData.stack.append(data)
