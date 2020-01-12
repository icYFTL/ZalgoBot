from source.databases.InternalBD import InternalBD
from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI
from source.vkapi.UserAPI import UserAPI


class SettingsInterface:
    @staticmethod
    def init(user_id) -> None:
        vk = BotAPI()
        token = InternalBD.get_token(user_id)
        if not token or not UserAPI.is_token_valid(token):
            token = "⛔"
            InternalBD.update_token(user_id, "")

        sub = InternalBD.getter(user_id)['subtype']
        if token:
            token = "✅"
        else:
            token = "⛔"

        vk.message_send(f"""Настройки.
    • AccessToken - {token}
    • Подписка - {sub}""", user_id, JSONWorker.read_json('settings'))
