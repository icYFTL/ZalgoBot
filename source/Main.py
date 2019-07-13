from source.BotApi import BotApi
from source.StaticData import StaticData
from source.LogWork import LogWork
from source.BDWorker import BDWorker
from source.CommandsHandler import CommandsHandler
from source.JSONWorker import JSONWorker


class Main:
    def __init__(self):
        self.botapi = BotApi()

    def handle(self):
        StaticData.trigger.wait()
        StaticData.trigger.clear()
        LogWork.add_note('info', 'Handling started')
        data = StaticData.stack.pop(0)
        if not BDWorker.user_exists(data['user_id']):
            BDWorker.add_user(data['user_id'])

        if len(data['message']) > 100:
            self.botapi.message_send(
                'Похоже, вы отправили сообщение длина которого {}.\nТак делать плохо, мы его обрезали до 100 символов.'.format(
                    str(len(data['message']))), data['user_id'], None)
            data['message'] = data['message'][:100]

        if '/' in str(data['message']):
            LogWork.add_note('info', 'It\'s a command {} from {}'.format(data['message'], data['user_id']))
            CH = CommandsHandler(data['user_id'])
            CH.identify_comma(data['message'])
            LogWork.add_note('info', 'Command handled')
            return

        LogWork.add_note('info', '"{}" message from {} was handled'.format(data['message'], data['user_id']))
        if data['message']:
            conf = BDWorker.getter(data['user_id'])
            if conf.get('current_mode') == 'zalgo':
                self.botapi.message_send_zalgo(data['message'], data['user_id'], JSONWorker.read_json('zalgokey.json'))
                BDWorker.messages_increment(data['user_id'])
            elif conf.get('current_mode') == 'flip':
                self.botapi.message_send_flip(data['message'], data['user_id'], JSONWorker.read_json('flipkey.json'))
                BDWorker.messages_increment(data['user_id'])
            elif conf.get('current_mode') == 'reverse':
                self.botapi.message_send_reverse(data['message'], data['user_id'],
                                                 JSONWorker.read_json('reversekey.json'))
                BDWorker.messages_increment(data['user_id'])
            elif conf.get('current_mode') == 'cout':
                self.botapi.message_send_cout(data['message'], data['user_id'], JSONWorker.read_json('coutkey.json'))
                BDWorker.messages_increment(data['user_id'])

        else:
            self.botapi.message_send('Гони текст, а не вот это всё.', data['user_id'], None)
