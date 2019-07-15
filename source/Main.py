from source.CommandsHandler import CommandsHandler
from source.LogWork import LogWork
from source.StaticData import StaticData
from source.databases.InternalBD import InternalBD
from source.interfaces.IntroInterface import IntroInterface
from source.texthandlers.MessageHandler import MessageHandler
from source.vkapi.BotAPI import BotAPI


class Main:
    def __init__(self):
        self.botapi = BotAPI()

    def handle(self):
        StaticData.trigger.wait()
        StaticData.trigger.clear()
        LogWork.add_note('info', 'Handling started')
        data = StaticData.stack_messages.pop(0)
        if data['message']:
            if not InternalBD.user_exists(data['user_id']):
                InternalBD.add_user(data['user_id'])
                IntroInterface.init(data['user_id'])
                return

            for waiter in range(len(StaticData.stack_waiters)):
                if data['user_id'] == StaticData.stack_waiters[waiter]['user_id']:
                    if StaticData.stack_waiters[waiter]['module'] == 'GPL':
                        CH = CommandsHandler(data['user_id'])
                        CH.gpl_comma(data['message'])
                        del (StaticData.stack_waiters[waiter])
                        return
                    elif StaticData.stack_waiters[waiter]['module'] == 'GPL.task':
                        CH = CommandsHandler(data['user_id'])
                        CH.module_wait_comma('GPL.task')
                        print(StaticData.stack_waiters)
                        return

            if '/' in str(data['message']):
                LogWork.add_note('info', 'It\'s a command {} from {}'.format(data['message'], data['user_id']))
                CH = CommandsHandler(data['user_id'])
                CH.identify_comma(data['message'])
                LogWork.add_note('info', 'Command handled')
                return

            if len(data['message']) > 100:
                self.botapi.message_send(
                    'Похоже, вы отправили сообщение длина которого {}.\nТак делать плохо, мы его обрезали до 100 символов.'.format(
                        str(len(data['message']))), data['user_id'], None)
                data['message'] = data['message'][:100]

            MH = MessageHandler(data['user_id'])
            MH.init(data)
        else:
            self.botapi.message_send('Гони текст, а не вот это всё.', data['user_id'], None)
