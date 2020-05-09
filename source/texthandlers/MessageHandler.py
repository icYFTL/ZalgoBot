import logging

from source.databases.InternalDB import InternalDB
from source.vkapi.BotAPI import BotAPI


class MessageHandler:
    @staticmethod
    def init(user_id: int, message: str) -> None:
        vk = BotAPI()
        IDB = InternalDB()
        user = IDB.get_user(user_id)

        vk.message_send(message=message, user_id=user_id, type_t=user['current_mode'])
        IDB.messages_increment(user['user_id'])

        logging.info('"{}" message from {} was handled using method {}'.format(message, user['user_id'],
                                                                               user['current_mode']))
