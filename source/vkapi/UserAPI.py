import json

import vk_api


class UserAPI:
    @staticmethod
    def is_token_valid(token) -> bool:
        try:
            vk = vk_api.VkApi(token=token)
            vk.method('friends.get')
            return True
        except:
            return False

    @staticmethod
    def user_exists(token, user_id) -> bool:
        vk = vk_api.VkApi(token=token)
        try:
            user = vk.method("users.get", {'user_ids': user_id})
            if not user[0].get('deactivated', False):
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def user_broken(token, user_id) -> bool:
        vk = vk_api.VkApi(token=token)
        data = vk.method("users.get", {'user_ids': user_id})[0]
        return data.get('can_access_closed') == False or data.get('deactivated')

    @staticmethod
    def get_id_from_url(token, url):
        try:
            url = url.replace("https://vk.com/", "").replace("vk.com/", "").replace("/", "")
            vk = vk_api.VkApi(token=token)
            return vk.method("users.get", {"user_ids": url})[0]['id']
        except:
            return "BadID"

    @staticmethod
    def user_get(token, user_id) -> json:
        vk = vk_api.VkApi(token=token)
        return vk.method("users.get", {"user_ids": user_id})
