import threading
from threading import Thread

from source.JSONWorker import JSONWorker
from source.StaticData import StaticData
from source.vkapi.BotAPI import BotAPI


class ModuleThread(Thread):
    trigger = threading.Event()

    def __init__(self, victim_id, subclass, user_id):
        Thread.__init__(self)
        self.victim_id = victim_id
        self.subclass = subclass
        self.user_id = user_id

    def run(self):
        vk = BotAPI()
        vk.message_send(message="Началась обработка ваших друзей. Пожалуйста, дождитесь ее конца.",
                        user_id=self.user_id, keyboard=JSONWorker.read_json('wait'))
        self.subclass.gpl_execute(victim_id=self.victim_id, user_id=self.user_id)
        ModuleThread.trigger.wait()
        ModuleThread.trigger.clear()
        for i in range(len(StaticData.stack_module_repls)):
            print(StaticData.stack_module_repls)
            if StaticData.stack_module_repls[i]['user_id'] == self.user_id:
                vk.message_send(message='Успешно завершено:\n' + ''.join(StaticData.stack_module_repls[i]['repl']),
                                user_id=self.user_id,
                                keyboard=JSONWorker.read_json('default'))
                for i in range(len(StaticData.stack_module_repls)):
                    if StaticData.stack_module_repls[i]['user_id'] == self.user_id:
                        del (StaticData.stack_module_repls[i])
                        break
                for i in range(len(StaticData.stack_waiters)):
                    if StaticData.stack_waiters[i]['user_id'] == self.user_id:
                        del (StaticData.stack_waiters[i])
                        break
                break
