import logging
from os import _exit
from threading import Thread

from source.databases.InternalDB import InternalDB
from source.interfaces.ServiceInterface import ServiceInterface
from source.main.CommandsHandler import CommandsHandler
from source.static.StaticData import StaticData
from source.texthandlers.MessageHandler import MessageHandler
from source.tools.json import getMessage
from source.vkapi.BotAPI import BotAPI


# TODO: REFACTOR & OPTIMIZE

class Main(Thread):
    def run(self):
        logging.info('Messages handler started')
        while True:
            try:
                vk = BotAPI()
                IDB = InternalDB()
                StaticData.new_message_trigger.wait()
                StaticData.new_message_trigger.clear()

                data = StaticData.stack_messages.pop(0)

                user_id = data['user_id']
                message = data['message']
                payload = data['payload']

                logging.info(f'Got "{message}" from {user_id}')

                CH = CommandsHandler(user_id)
                if message:
                    if not IDB.user_exists(user_id):
                        IDB.add_user(user_id)
                        ServiceInterface.start(user_id)
                        continue

                    data = IDB.get_user(user_id)
                    if data['status']:
                        if payload == '/back':
                            IDB.status_changer(user_id=user_id, status=None)
                            CH.back_comma()
                            continue
                        logging.info('Module "{}" request from {}'.format(data['status'], user_id))

                        del IDB

                        # GPL
                        if 'GPL' in data['status'] and payload == '/GPL_run':
                            CH.gpl_run_comma()
                        elif 'GPL' in data['status']:
                            CH.gpl_run_comma(message)
                        continue

                    if payload:
                        logging.info(f'Command "{payload}" request from {user_id}')
                        CH.identify_comma(payload)
                        continue

                    if len(message) > 100:
                        vk.message_send(getMessage('max_message_length_note').format(length=str(len(message))),
                                        user_id=user_id)

                    MessageHandler.init(user_id, message[:100])
                else:
                    logging.warning("Bad message from {}".format(user_id))
                    vk.message_send(message=getMessage('text_unset'), user_id=user_id)
            except KeyboardInterrupt:
                _exit(0)
