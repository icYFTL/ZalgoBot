from source.databases.InternalBD import InternalBD
from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI
from source.vkapi.UserAPI import UserAPI


class SettingsInterface:
    @staticmethod
    def init(user_id) -> None:
        vk = BotAPI()
        token = InternalBD.get_token(user_id)

        sub = InternalBD.getter(user_id)['subtype']
        if not token or not UserAPI.is_token_valid(token):
            token = '⛔'
            InternalBD.update_token(user_id, '')
        else:
            token = '✅'

        vk.message_send(f'''Настройки.
    • AccessToken - {token}
    • Подписка - {sub}''', user_id, JSONWorker.keyboard_handler('settings'))

    @staticmethod
    def about(user_id) -> None:
        from source.static.StaticData import StaticData
        vk = BotAPI()
        vk.message_send(f'ZalgoBot v{StaticData.version}\nBy [id239125937|icYFTL]\nhttps://github.com/icYFTL/ZalgoBot',
                        user_id)

    @staticmethod
    def access_token(user_id) -> None:
        vk = BotAPI()
        vk.message_send('''Чтобы пользоваться некоторыми штуками, увы, нужен access token.

        Access token - это объект, который позволяет пользоваться некоторыми способностями конкретно вашего аккаунта.
        Например - смотреть ваших друзей.

        Зарегистрировать свой токен в нашей системе можно перейдя по ссылке: https://vk.cc/aikRxw''',
                        user_id, JSONWorker.keyboard_handler('default'))
