from threading import Thread
import hues

from source.iniWorker import iniWorker
from source.CommandsHandler import CommandsHandler
from source.StaticData import StaticData
from source.BotApi import BotApi
from Config import Config
from source.JSONWorker import JSONWorker


class Threads(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.botapi = BotApi(Config.access_token)

    def run(self):
        while True:
            if StaticData.stack:
                hues.log('Handling started')
                data = StaticData.stack.pop(0)
                if not iniWorker.user_exists(data[1]):
                    iniWorker.createConfig(data[1])

                data = data[:50]

                hues.log('It\'s a command {} from {}'.format(data[0], data[1]))
                if '/' in str(data[0]):
                    CH = CommandsHandler(data[1])
                    CH.identify_comma(data[0])
                    hues.log('Command handled')
                    continue

                hues.log('{} message from {} was handled'.format(data[0], data[1]))
                if data[0]:
                    conf = iniWorker.readConfig(data[1])
                    if conf[0] == 'zalgo':
                        self.botapi.message_send_zalgo(data[0], data[1], JSONWorker.read_json('zalgokey.json'))
                        iniWorker.changeConfig(data[1], 'messages_count',
                                               str(int(iniWorker.readConfig(data[1])[3]) + 1))
                    elif conf[0] == 'flip':
                        self.botapi.message_send_flip(data[0], data[1], JSONWorker.read_json('flipkey.json'))
                        iniWorker.changeConfig(data[1], 'messages_count',
                                               str(int(iniWorker.readConfig(data[1])[3]) + 1))
                    elif conf[0] == 'reverse':
                        self.botapi.message_send_reverse(data[0], data[1], JSONWorker.read_json('reversekey.json'))
                        iniWorker.changeConfig(data[1], 'messages_count',
                                               str(int(iniWorker.readConfig(data[1])[3]) + 1))
                else:
                    self.botapi.message_send('Гони текст, а не вот это всё.', data[1], None)
