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
        vk.message_send(
            message='''Aurora это модуль, позволяющий удалять подписки на удаливших вас друзей.
Подключить модуль можно нажав на клавиатуре /aurora_add
Отключить модуль можно нажав на клавиатуре /aurora_remove
''',
            user_id=user_id, keyboard=JSONWorker.read_json('aurora'))

    @staticmethod
    def add(user_id):
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
        from source.modules.Aurora.source.databases.InternalBD import InternalBD
        if InternalBD.user_exists(user_id):
            vk.message_send(message="Вы уже подключили модуль Aurora.", user_id=user_id,
                            keyboard=JSONWorker.read_json('aurora'))
            return
        InternalBD.add_user(user_id, token)
        vk.message_send(message="Aurora временно не работает.", user_id=user_id,
                        keyboard=JSONWorker.read_json('aurora'))

    @staticmethod
    def remove(user_id):
        vk = BotAPI()
        from source.modules.Aurora.source.databases.InternalBD import InternalBD
        if not InternalBD.user_exists(user_id):
            vk.message_send(message="Вы не подключали модуль Aurora.", user_id=user_id,
                            keyboard=JSONWorker.read_json('aurora'))
            return
        InternalBD.delete_user(user_id)
        vk.message_send(message="Вы успешно отключили модуль Aurora!", user_id=user_id,
                        keyboard=JSONWorker.read_json('aurora'))

    @staticmethod
    def statistic(user_id):
        pass  # Await for active users
