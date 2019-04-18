from Config import Config
from source.iniWorker import iniWorker
from source.CommandsHandler import CommandsHandler
from source.BotApi import BotApi


class ApiWorker:
    def __init__(self):
        self.token = Config.access_token
        self.botapi = BotApi(self.token)
        self.started()

    def started(self):
        for admin in Config.admins:
            self.botapi.message_send('Скрипт начал работу.', admin, False)

    def get_message(self):
        data = self.botapi.message_handler()

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
