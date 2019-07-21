from threading import Thread

from source.databases.InternalBD import InternalBD
from source.modules.GPL.source.StaticData import StaticData as ModuleInfo
from source.modules.ModulesController import ModulesController
from source.other.JSONWorker import JSONWorker
from source.vkapi.BotAPI import BotAPI
from source.vkapi.TokenController import TokenController
from source.vkapi.UserAPI import UserAPI


class GPLInterface:
    @staticmethod
    def init(user_id, victim_id=None):
        vk = BotAPI()
        token = InternalBD.getter(user_id)['token']
        TC = TokenController(token)

        if not victim_id:
            vk.message_send(message='Введите ссылку на страницу пользователя:',
                            user_id=user_id)
            InternalBD.changer(user_id=user_id, obj=['status', 'GPL_P_G'])
            return
        elif not TokenController.token_exists(user_id):
            vk.message_send('Вы не установили access token в настройках.',
                            user_id=user_id, keyboard=JSONWorker.read_json('settings'))
            InternalBD.changer(user_id=user_id, obj=['status', None])
            return
        elif not TC.token_valid():
            vk.message_send('Токен истек. Обновите его.',
                            user_id=user_id, keyboard=JSONWorker.read_json('settings'))
            InternalBD.changer(user_id=user_id, obj=['status', None])
            return
        elif not TC.user_exists(UserAPI.get_id_from_url(token, victim_id)):
            vk.message_send('Неверный user_id.',
                            user_id=user_id, keyboard=JSONWorker.read_json('modules'))
            InternalBD.changer(user_id=user_id, obj=['status', None])
            return
        elif UserAPI.user_closed(token, UserAPI.get_id_from_url(token, victim_id)):
            vk.message_send('У данного пользователя закрытый профиль.\nПолучить друзей не является возможным.',
                            user_id=user_id, keyboard=JSONWorker.read_json('modules'))
            InternalBD.changer(user_id=user_id, obj=['status', None])
            return
        GPLInterface.run(UserAPI.get_id_from_url(token, victim_id), user_id, token)

    @staticmethod
    def run(victim_id, user_id, token):
        MC = ModulesController(user_id, token)
        thread = Thread(target=MC.gpl_execute, args=(victim_id,))
        thread.start()

    @staticmethod
    def wait_task(user_id, module):
        vk = BotAPI()
        percentage = ModuleInfo.percent
        vk.message_send(message='{module} в данный момент выполняется ({perc})'.format(module=module, perc=percentage),
                        user_id=user_id)
