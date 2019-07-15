import source.modules.GPL.GPL
from source.ModuleThread import ModuleThread
from source.StaticData import StaticData
from source.databases.InternalBD import InternalBD
from source.vkapi.UserAPI import UserAPI


class ModulesController:
    def __init__(self, user_id):
        self.user_id = user_id
        self.token = self.token_exists()

    def token_exists(self):
        token = InternalBD.get_token(self.user_id)
        if token:
            return token
        else:
            return False

    def token_valid(self):
        UA = UserAPI(self.token)
        try:
            UA.get_session()
            return True
        except:
            return False

    def user_exists(self, user):
        UA = UserAPI(self.token)
        UA.get_session()
        return UA.user_exists(user)

    def gpl_execute(self, victim_id, user_id):
        gpl = source.modules.GPL.GPL.GPL()
        StaticData.stack_waiters.append({'user_id': self.user_id, 'module': 'GPL.task'})
        StaticData.stack_module_repls.append(
            {'module': 'GPL', 'repl': gpl.main({'access': self.token, 'user_id': [victim_id]}), 'user_id': user_id})
        ModuleThread.trigger.set()
