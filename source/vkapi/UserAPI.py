import vk_api
import vk_api.exceptions


class UserAPI:
    def __init__(self, token):
        self.token = token
        self.vk = None

    def get_session(self):
        try:
            self.vk = vk_api.VkApi(token=self.token)
            return True
        except:
            return False

    def user_exists(self, user_id):
        try:
            if self.vk.method("users.get", {'user_ids': user_id})[0]['first_name'] == 'DELETED':
                return False
            return True
        except:
            return False
