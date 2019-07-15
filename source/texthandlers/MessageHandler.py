from source.LogWork import LogWork
from source.databases.InternalBD import InternalBD
from source.vkapi.BotAPI import BotAPI


class MessageHandler:
    def __init__(self, user_id):
        self.user_id = user_id
        self.vk = BotAPI()

    def init(self, data):
        conf = InternalBD.getter(data['user_id'])
        if conf['current_mode'] == 'zalgo':
            self.vk.message_send(message=data['message'], user_id=data['user_id'], type_t='zalgo')
        elif conf['current_mode'] == 'flip':
            self.vk.message_send(message=data['message'], user_id=data['user_id'], type_t='flip')
        elif conf['current_mode'] == 'reverse':
            self.vk.message_send(message=data['message'], user_id=data['user_id'], type_t='reverse')
        elif conf['current_mode'] == 'cout':
            self.vk.message_send(message=data['message'], user_id=data['user_id'], type_t='cout')
        InternalBD.messages_increment(data['user_id'])
        LogWork.add_note('info',
                         '"{}" message from {} was handled using method {}'.format(data['message'], data['user_id'],
                                                                                   conf['current_mode']))
