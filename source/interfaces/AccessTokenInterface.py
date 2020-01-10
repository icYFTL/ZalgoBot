from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class AccessTokenInterface:
    @staticmethod
    def init(user_id) -> None:
        vk = BotAPI()
        vk.message_send('''Чтобы пользоваться некоторыми штуками, увы, нужен access token.
        
Access token - это объект, который позволяет пользоваться некоторыми способностями конкретно вашего аккаунта.
Например - смотреть ваших друзей.
        
Зарегистрировать свой токен в нашей системе можно перейдя по ссылке: https://vk.cc/a3BQFY''',
                        user_id, JSONWorker.read_json('default'))
