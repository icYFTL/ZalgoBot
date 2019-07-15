from source.JSONWorker import JSONWorker
from source.databases.InternalBD import InternalBD
from source.vkapi.BotAPI import BotAPI


class SettingsInterface:
    @staticmethod
    def init(user_id):
        vk = BotAPI()
        token = InternalBD.get_token(user_id)
        sub = InternalBD.getter(user_id)['status']
        if token:
            token = "✅"
        else:
            token = "⛔"
        if sub == 0:
            sub = "Базовая"

        vk.message_send("""Настройки.
        • AccessToken - {}
        • Подписка - {}""".format(token, sub), user_id, JSONWorker.read_json('settings'))
