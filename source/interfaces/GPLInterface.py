from source.JSONWorker import JSONWorker
from source.ModuleThread import ModuleThread
from source.ModulesController import ModulesController
from source.StaticData import StaticData
from source.modules.GPL.source.StaticData import StaticData as ModuleInfo
from source.vkapi.BotAPI import BotAPI


class GPLInterface:
    @staticmethod
    def init(user_id, victim_id=None):
        vk = BotAPI()
        MC = ModulesController(user_id)

        if not victim_id:
            vk.message_send(message='Введите ID пользователя:',
                            user_id=user_id)
            StaticData.stack_waiters.append({'user_id': user_id, 'module': 'GPL'})
        elif not MC.token_exists():
            vk.message_send('Вы не установили access token в настройках.',
                            user_id=user_id, keyboard=JSONWorker.read_json('settings'))
        elif not MC.token_valid():
            vk.message_send('Токен истек. Обновите его.',
                            user_id=user_id, keyboard=JSONWorker.read_json('settings'))
        elif not MC.user_exists(victim_id):
            vk.message_send('Неверный user_id.',
                            user_id=user_id, keyboard=JSONWorker.read_json('modules'))
        else:
            GPLInterface.run(victim_id, MC, user_id)

    @staticmethod
    def run(victim_id, subclass, user_id):
        thread = ModuleThread(victim_id, subclass, user_id)
        thread.start()

    @staticmethod
    def wait_task(user_id, module):
        vk = BotAPI()
        percentage = ModuleInfo.percent
        vk.message_send(message='{module} в данный момент выполняется ({perc})'.format(module=module, perc=percentage),
                        user_id=user_id)
