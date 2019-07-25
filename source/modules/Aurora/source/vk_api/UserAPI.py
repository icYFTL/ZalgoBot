import vk_api


class UserAPI:
    def __init__(self, token):
        self.token = token
        self.vk = self.get_session()

    def get_session(self):
        return vk_api.VkApi(token=self.token)

    def get_friends(self):
        return self.vk.method("friends.get")

    def get_subs(self):
        return self.vk.method("friends.getRequests", {'out': 1})

    def unsub(self, user_id):
        self.vk.method("friends.delete", {'user_id': user_id})
