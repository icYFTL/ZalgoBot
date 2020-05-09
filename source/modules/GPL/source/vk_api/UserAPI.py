import re

import vk_api


class UserAPI:

    def __init__(self, user_id, token):
        self.token = token
        self.user_id = self.get_id_from_url(user_id)
        self.vk = self.get_session()

    def get_session(self):
        try:
            return vk_api.VkApi(token=self.token)
        except:
            exit()

    def get_friends(self):
        try:
            return self.vk.method('friends.get', {'user_id': self.user_id}).get('items')
        except:
            return False

    def get_info(self, user_ids):
        return self.vk.method('users.get', {'user_ids': ','.join("{0}".format(n) for n in user_ids),
                                            'fields': 'city,schools,education'})

    def get_id_from_url(self, url):
        try:
            int(url)
            return url
        except:
            try:
                url = re.sub(r"(https://)?vk.com/", '', url).replace('/', '')
                vk = vk_api.VkApi(token=self.token)
                return vk.method("users.get", {"user_ids": url})[0]['id']
            except:
                return False
