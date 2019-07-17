from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI


class AccessTokenInterface:
    @staticmethod
    def init(user_id):
        vk = BotAPI()
        vk.message_send('''Чтобы пользоваться некоторыми штуками, увы, нужен access token.
        
        Access token - это объект, который позволяет пользоваться некоторыми способностями конкретно вашего аккаунта.
        Например - смотреть ваших друзей.
        
        Вы даете согласие на использование своего токена во многих местах, но просто этого не замечаете.
        
        При запросе токена ВК говорит вам о том что будет затронуто.
        
        Конкретно наши модули не несут никакого вреда вашему аккаунту и делают только то, что должны.
        
        Зарегистрировать свой токен в нашей системе можно перейдя по ссылке: https://vk.cc/9B11jR''',
                        user_id, JSONWorker.read_json('default'))
