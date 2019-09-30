from source.databases.InternalBD import InternalBD as IB
from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI
from source.vkapi.TokenController import TokenController


class AuroraInterface:
    @staticmethod
    def init(user_id):
        vk = BotAPI()
        vk.message_send(message="Aurora временно недоступна(", user_id=user_id)
        return
        token = IB.getter(user_id)['token']
        TC = TokenController(token)

        if not TokenController.token_exists(user_id):
            vk.message_send('Вы не установили access token в настройках.',
                            user_id=user_id, keyboard=JSONWorker.read_json('settings'))
            IB.status_changer(user_id=user_id, obj="None")
            return
        elif not TC.token_valid():
            vk.message_send('Токен истек. Обновите его.',
                            user_id=user_id, keyboard=JSONWorker.read_json('settings'))
            IB.status_changer(user_id=user_id, obj="None")
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
        vk.message_send(message="Aurora временно недоступна(", user_id=user_id)
        return
        token = IB.getter(user_id)['token']
        TC = TokenController(token)

        if not TokenController.token_exists(user_id):
            vk.message_send('Вы не установили access token в настройках.',
                            user_id=user_id, keyboard=JSONWorker.read_json('settings'))
            IB.status_changer(user_id=user_id, obj="None")
            return
        elif not TC.token_valid():
            vk.message_send('Токен истек. Обновите его.',
                            user_id=user_id, keyboard=JSONWorker.read_json('settings'))
            IB.status_changer(user_id=user_id, obj="None")
            return
        from source.modules.Aurora.source.databases.InternalBD import InternalBD
        if InternalBD.user_exists(user_id):
            vk.message_send(message="Вы уже подключили модуль Aurora.", user_id=user_id,
                            keyboard=JSONWorker.read_json('aurora'))
            return
        InternalBD.add_user(user_id, token)
        vk.message_send(message="Вы успешно подключили модуль Aurora!", user_id=user_id,
                        keyboard=JSONWorker.read_json('aurora'))

    @staticmethod
    def remove(user_id):
        vk = BotAPI()
        vk.message_send(message="Aurora временно недоступна(", user_id=user_id)
        return
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
