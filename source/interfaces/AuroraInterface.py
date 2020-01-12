from source.databases.InternalBD import InternalBD
from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI
from source.vkapi.UserAPI import UserAPI

class AuroraInterface:
    @staticmethod
    def init(user_id) -> None:
        vk = BotAPI()
        vk.message_send('Увы, Aurora в данный момент недоступна.',
                        user_id=user_id, keyboard=JSONWorker.keyboard_handler('settings'))
        return

        token = InternalBD.getter(user_id)['token']

        if not InternalBD.get_token(user_id):
            vk.message_send('Вы не установили access token в настройках.',
                            user_id=user_id, keyboard=JSONWorker.keyboard_handler('settings'))
            InternalBD.status_changer(user_id=user_id, obj="None")
            return
        elif not UserAPI.is_token_valid(token):
            vk.message_send('Токен истек. Обновите его.',
                            user_id=user_id, keyboard=JSONWorker.keyboard_handler('settings'))
            InternalBD.status_changer(user_id=user_id, obj="None")
            return
        vk.message_send(
            message='''Aurora это модуль, позволяющий удалять подписки на удаливших вас друзей.
Подключить модуль можно нажав на клавиатуре /aurora_add
Отключить модуль можно нажав на клавиатуре /aurora_remove
''',
            user_id=user_id, keyboard=JSONWorker.keyboard_handler('aurora'))

    @staticmethod
    def add(user_id) -> None:
        vk = BotAPI()
        vk.message_send('Увы, Aurora в данный момент недоступна.',
                        user_id=user_id, keyboard=JSONWorker.keyboard_handler('settings'))
        return
        token = InternalBD.getter(user_id)['token']

        if not InternalBD.get_token(token):
            vk.message_send('Вы не установили access token в настройках.',
                            user_id=user_id, keyboard=JSONWorker.keyboard_handler('settings'))
            InternalBD.status_changer(user_id=user_id, obj="None")
            return
        elif not UserAPI.is_token_valid(token):
            vk.message_send('Токен истек. Обновите его.',
                            user_id=user_id, keyboard=JSONWorker.keyboard_handler('settings'))
            InternalBD.status_changer(user_id=user_id, obj="None")
            return
        from source.modules.Aurora.source.databases.InternalBD import InternalBD as IB
        if IB.user_exists(user_id):
            vk.message_send(message="Вы уже подключили модуль Aurora.", user_id=user_id,
                            keyboard=JSONWorker.keyboard_handler('aurora'))
            return
        IB.add_user(user_id, token)
        vk.message_send(message="Вы успешно подключили модуль Aurora!", user_id=user_id,
                        keyboard=JSONWorker.keyboard_handler('aurora'))

    @staticmethod
    def remove(user_id) -> None:
        vk = BotAPI()
        vk.message_send('Увы, Aurora в данный момент недоступна.',
                        user_id=user_id, keyboard=JSONWorker.keyboard_handler('settings'))
        return
        from source.modules.Aurora.source.databases.InternalBD import InternalBD as IB
        if not IB.user_exists(user_id):
            vk.message_send(message="Вы не подключали модуль Aurora.", user_id=user_id,
                            keyboard=JSONWorker.keyboard_handler('aurora'))
            return
        IB.delete_user(user_id)
        vk.message_send(message="Вы успешно отключили модуль Aurora!", user_id=user_id,
                        keyboard=JSONWorker.keyboard_handler('aurora'))

    @staticmethod
    def statistic(user_id) -> None:
        pass  # Await for active users
