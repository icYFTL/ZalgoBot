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

    @staticmethod
    def user_closed(token, user_id):
        vk = vk_api.VkApi(token=token)
        return vk.method("users.get", {'user_ids': user_id})[0]['is_closed']

    @staticmethod
    def get_id_from_url(token, url):
        url = url.replace("https://vk.com/", "").replace("/", "")
        vk = vk_api.VkApi(token=token)
        return vk.method("users.get", {"user_ids": url})[0]['id']
