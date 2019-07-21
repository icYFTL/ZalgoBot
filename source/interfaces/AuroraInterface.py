from source.databases.InternalBD import InternalBD as IB
from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI
from source.vkapi.TokenController import TokenController


class AuroraInterface:
    @staticmethod
    def init(user_id):
        vk = BotAPI()
        token = IB.getter(user_id)['token']
        TC = TokenController(token)

        if not TokenController.token_exists(user_id):
            vk.message_send('Вы не установили access token в настройках.',
                            user_id=user_id, keyboard=JSONWorker.read_json('settings'))
            IB.changer(user_id=user_id, obj=['status', None])
            return
        elif not TC.token_valid():
            vk.message_send('Токен истек. Обновите его.',
                            user_id=user_id, keyboard=JSONWorker.read_json('settings'))
            IB.changer(user_id=user_id, obj=['status', None])
            return
        from source.modules.Aurora.source.vkapi.UserAPI import UserAPI
        ua_legit = UserAPI(token)
        from source.modules.Aurora.source.databases.InternalBD import InternalBD
        InternalBD.add_user(user_id, ','.join(ua_legit.get_requests()[0]['items']), token)
