from source.databases.InternalBD import InternalBD
from source.interfaces.IntroInterface import IntroInterface
from source.logger.LogWork import LogWork
from source.main.CommandsHandler import CommandsHandler
from source.static.StaticData import StaticData
from source.texthandlers.MessageHandler import MessageHandler
from source.vkapi.BotAPI import BotAPI


class Main:
    @staticmethod
    def handle():
        LogWork.log('Messages handler has been started')
        while True:
            vk = BotAPI()
            StaticData.new_message_trigger.wait()
            StaticData.new_message_trigger.clear()

            data = StaticData.stack_messages.pop(0)
            user_id = data['user_id']
            message = data['message']

            LogWork.log('Got "{message}" from {user_id}'.format(message=message, user_id=user_id))

            CH = CommandsHandler(user_id)
            if message:
                if not InternalBD.user_exists(user_id):
                    InternalBD.add_user(user_id)
                    IntroInterface.init(user_id)
                    continue

                data = InternalBD.getter(user_id)
                if data['status'] != "None":
                    if message == '/back':
                        InternalBD.changer(user_id, ['status', None])
                        CH.back_comma()
                        continue
                    LogWork.log('Module "{}" request from {}'.format(data['status'], user_id))

                    # GPL
                    if 'GPL' in data['status'] and message == '/GPL':
                        CH.gpl_comma()
                    elif 'GPL' in data['status']:
                        CH.gpl_comma(message)
                    elif 'WFM' in data['status']:
                        CH.get_status_comma()
                    continue

                if str(message)[0] == '/':
                    LogWork.log('Command "{}" request from {}'.format(message, user_id))
                    CH.identify_comma(message)
                    continue

                if len(message) > 100:
                    vk.message_send(
                        message='Длина вашего сообщения {}.\nМаксимально допустимая длина: 100 символов.'.format(
                            str(len(message))), user_id=user_id)
                    message = message[:100]

                MessageHandler.init(
                    {'user_id': user_id, 'message': message, 'current_mode': data['current_mode']})
            else:
                LogWork.log("Bad message from {}".format(user_id))
                vk.message_send(message='Гони текст, а не вот это всё.', user_id=user_id)
