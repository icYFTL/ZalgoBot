from source.databases.InternalBD import InternalBD
from source.logger.LogWork import LogWork
from source.vkapi.BotAPI import BotAPI


class MessageHandler:
    @staticmethod
    def init(data) -> None:
        vk = BotAPI()
        conf = InternalBD.getter(data['user_id'])
        if conf['current_mode'] == 'zalgo':
            vk.message_send(message=data['message'], user_id=data['user_id'], type_t='zalgo')
        elif conf['current_mode'] == 'flip':
            vk.message_send(message=data['message'], user_id=data['user_id'], type_t='flip')
        elif conf['current_mode'] == 'reverse':
            vk.message_send(message=data['message'], user_id=data['user_id'], type_t='reverse')
        elif conf['current_mode'] == 'cout':
            vk.message_send(message=data['message'], user_id=data['user_id'], type_t='cout')
        elif conf['current_mode'] == 'white_bracket':
            vk.message_send(message=data['message'], user_id=data['user_id'], type_t='white_bracket')
        InternalBD.messages_increment(data['user_id'])
        LogWork.log('"{}" message from {} was handled using method {}'.format(data['message'], data['user_id'],
                                                                              conf['current_mode']))
