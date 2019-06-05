from threading import Thread

from Config import Config
from source.BDWorker import BDWorker
from source.BotApi import BotApi
from source.CommandsHandler import CommandsHandler
from source.JSONWorker import JSONWorker
from source.LogWork import LogWork
from source.StaticData import StaticData


class Threads(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.botapi = BotApi(Config.access_token)

    def run(self):
        while True:
            if StaticData.stack:
                LogWork.add_note('info', 'Handling started')
                data = StaticData.stack.pop(0)
                if not BDWorker.user_exists(data[1]):
                    BDWorker.add_user(data[1])

                if len(data[0]) > 100:
                    self.botapi.message_send(
                        'Похоже, вы отправили сообщение длина которого {}.\nТак делать плохо, мы его обрезали до 100 символов.'.format(
                            str(len(data[0]))), data[1], None)
                    data[0] = data[0][:100]

                if '/' in str(data[0]):
                    LogWork.add_note('info', 'It\'s a command {} from {}'.format(data[0], data[1]))
                    CH = CommandsHandler(data[1])
                    CH.identify_comma(data[0])
                    LogWork.add_note('info', 'Command handled')
                    continue

                LogWork.add_note('info', '"{}" message from {} was handled'.format(data[0], data[1]))
                if data[0]:
                    conf = BDWorker.getter(data[1])
                    if conf.get('current_mode') == 'zalgo':
                        self.botapi.message_send_zalgo(data[0], data[1], JSONWorker.read_json('zalgokey.json'))
                        BDWorker.messages_increment(data[1])
                    elif conf.get('current_mode') == 'flip':
                        self.botapi.message_send_flip(data[0], data[1], JSONWorker.read_json('flipkey.json'))
                        BDWorker.messages_increment(data[1])
                    elif conf.get('current_mode') == 'reverse':
                        self.botapi.message_send_reverse(data[0], data[1], JSONWorker.read_json('reversekey.json'))
                        BDWorker.messages_increment(data[1])
                    elif conf.get('current_mode') == 'cout':
                        self.botapi.message_send_cout(data[0], data[1], JSONWorker.read_json('coutkey.json'))
                        BDWorker.messages_increment(data[1])

                else:
                    self.botapi.message_send('Гони текст, а не вот это всё.', data[1], None)
