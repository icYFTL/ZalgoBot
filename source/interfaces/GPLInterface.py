from threading import Thread

from source.databases.InternalBD import InternalBD
from source.modules.ModulesController import ModulesController
from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI
from source.vkapi.UserAPI import UserAPI


class GPLInterface:
    @staticmethod
    def init(user_id) -> None:
        vk = BotAPI()
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
        vk.message_send(message='''GPL это модуль позволяющий узнать примерное место жительства человека по его друзьям.
Ведь все мы любим указывать школы, университеты итд.''', user_id=user_id, keyboard=JSONWorker.keyboard_handler('gpl'))

    @staticmethod
    def run(victim_id, user_id) -> None:
        token = InternalBD.getter(user_id)['token']
        vk = BotAPI()

        if not victim_id:
            vk.message_send(message='Введите ссылку на страницу пользователя:',
                            user_id=user_id)
            InternalBD.status_changer(user_id=user_id, obj="GPL_P_G")
            return

        victim_id = UserAPI.get_id_from_url(token, victim_id)

        if victim_id == "BadID":
            vk.message_send('Неверная ссылка.',
                            user_id=user_id, keyboard=JSONWorker.keyboard_handler('gpl'))
            InternalBD.status_changer(user_id=user_id, obj="None")
            return

        elif not UserAPI.user_exists(user_id=user_id, token=token):
            vk.message_send('Аккаунт невалиден.',
                            user_id=user_id, keyboard=JSONWorker.keyboard_handler('gpl'))
            InternalBD.status_changer(user_id=user_id, obj="None")
            return

        elif UserAPI.user_closed(token, UserAPI.get_id_from_url(token, victim_id)):
            vk.message_send(
                'У данного пользователя закрытый профиль или его не существует.\nПолучить друзей не является возможным.',
                user_id=user_id, keyboard=JSONWorker.keyboard_handler('gpl'))
            InternalBD.status_changer(user_id=user_id, obj="None")
            return

        MC = ModulesController(user_id, token)
        thread = Thread(target=MC.gpl_execute, args=(victim_id,))
        thread.start()
