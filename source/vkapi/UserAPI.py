import vk_api
import vk_api.exceptions


class UserAPI:
    def __init__(self, token):
        self.token = token
        self.vk = self.get_session()

    def get_session(self):
        try:
            return vk_api.VkApi(token=self.token)
        except:
            return False

    def user_exists(self, user_id):
        try:
            if self.vk.method("users.get", {'user_ids': user_id})[0]['first_name'] == 'DELETED':
                return False
            return True
        except:
            return False

    def user_closed(self, user_id):
        return self.vk.method("users.get", {'user_ids': user_id})[0]['is_closed']
