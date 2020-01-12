from source.databases.InternalBD import InternalBD
from source.interfaces.IntroInterface import IntroInterface
from source.logger.LogWork import LogWork
from source.main.CommandsHandler import CommandsHandler
from source.static.StaticData import StaticData
from source.texthandlers.MessageHandler import MessageHandler
from source.vkapi.BotAPI import BotAPI


class Main:
    @staticmethod
    def handle() -> None:
        LogWork.log('Messages handler has been started')
        while True:
            vk = BotAPI()
            StaticData.new_message_trigger.wait()
            StaticData.new_message_trigger.clear()

            data = StaticData.stack_messages.pop(0)

            user_id = data['user_id']
            message = data['message']
            payload = data['payload']

            LogWork.log(f'Got "{message}" from {user_id}')

            CH = CommandsHandler(user_id)
            if message:
                if not InternalBD.user_exists(user_id):
                    InternalBD.add_user(user_id)
                    IntroInterface.init(user_id)
                    continue

                data = InternalBD.getter(user_id)
                if data['status'] != "None":
                    if payload == '/back':
                        InternalBD.status_changer(user_id=user_id, obj="None")
                        CH.back_comma()
                        continue
                    LogWork.log('Module "{}" request from {}'.format(data['status'], user_id))

                    # GPL
                    if 'GPL' in data['status'] and payload == '/GPL_run':
                        CH.gpl_run_comma()
                    elif 'GPL' in data['status']:
                        CH.gpl_run_comma(message)
                    continue

                if payload:
                    LogWork.log(f'Command "{payload}" request from {user_id}')
                    CH.identify_comma(payload)
                    continue

                if len(message) > 100:
                    vk.message_send(message=f'''Длина вашего сообщения {str(
                        len(message))}.\nМаксимально допустимая длина: 100 символов.''', user_id=user_id)
                    message = message[:100]

                MessageHandler.init(
                    {'user_id': user_id, 'message': message, 'current_mode': data['current_mode']})
            else:
                LogWork.log("Bad message from {}".format(user_id))
                vk.message_send(message='Гони текст, а не вот это всё.', user_id=user_id)
