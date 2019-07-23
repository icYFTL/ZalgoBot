from source.databases.InternalBD import InternalBD
from source.interfaces.IntroInterface import IntroInterface
from source.main.CommandsHandler import CommandsHandler
from source.Logger.LogWork import LogWork
from Static.StaticData import StaticData
from source.texthandlers.MessageHandler import MessageHandler
from source.vkapi.BotAPI import BotAPI


class Main:
    def __init__(self):
        self.vk = BotAPI()
        self.user_id = None
        self.message = None

    def get_user_data(self):
        return InternalBD.getter(self.user_id)

    def handle(self):
        StaticData.new_message_trigger.wait()
        StaticData.new_message_trigger.clear()

        LogWork.log('Handling started')

        data = StaticData.stack_messages.pop(0)
        self.user_id = data['user_id']
        self.message = data['message']

        CH = CommandsHandler(self.user_id)
        if self.message:
            if not InternalBD.user_exists(self.user_id):
                InternalBD.add_user(self.user_id)
                IntroInterface.init(self.user_id)
                return

            data = InternalBD.getter(self.user_id)
            if data['status'] != "None":
                if self.message == '/back':
                    InternalBD.changer(self.user_id, ['status', None])
                    CH.back_comma()
                    return
                LogWork.log('Module "{}" request from {}'.format(data['status'], self.user_id))
                if 'GPL' in data['status'] and self.message == '/GPL':
                    CH.gpl_comma()
                elif 'GPL' in data['status']:
                    CH.gpl_comma(self.message)
                elif 'WFM' in data['status']:
                    if 'gpl.task' in data['status']:
                        import source.modules.GPL.source.StaticData
                        self.vk.message_send(
                            message="[GPL Module]\n{percent}\n{users} друзей обработано".format(
                                percent=source.modules.GPL.source.StaticData.StaticData.percent['percent'],
                                users=source.modules.GPL.source.StaticData.StaticData.percent['users']),
                            user_id=self.user_id)
                    else:
                        self.vk.message_send(message="В данный момент выполняется {}.\nПожалуйста, подождите.".format(
                            data['status'].replace('WFM', '')), user_id=self.user_id)
                return

            if '/' in str(self.message):
                LogWork.log('Command "{}" request from {}'.format(self.message, self.user_id))
                CH.identify_comma(self.message)
                return

            if len(self.message) > 100:
                self.vk.message_send(
                    message='Похоже, вы отправили сообщение длина которого {}.\nТак делать плохо, мы обрезали его до 100 символов.'.format(
                        str(len(self.message))), user_id=self.user_id)
                self.message = self.message[:100]

            MessageHandler.init(
                {'user_id': self.user_id, 'message': self.message, 'current_mode': data['current_mode']})
        else:
            self.vk.message_send(message='Гони текст, а не вот это всё.', user_id=self.user_id)
