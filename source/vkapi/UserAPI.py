import vk_api


class UserAPI:
    @staticmethod
    def is_token_valid(token):
        try:
            vk = vk_api.VkApi(token=token)
            vk.method('friends.get')
            return True
        except:
            return False

    @staticmethod
    def user_exists(token, user_id):
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
    def user_closed(token, user_id):
        vk = vk_api.VkApi(token=token)
        return vk.method("users.get", {'user_ids': user_id})[0].get('is_closed')

    @staticmethod
    def get_id_from_url(token, url):
        try:
            url = url.replace("https://vk.com/", "").replace("vk.com/", "").replace("/", "")
            vk = vk_api.VkApi(token=token)
            return vk.method("users.get", {"user_ids": url})[0]['id']
        except:
            return "BadID"

    @staticmethod
    def user_get(token, user_id):
        vk = vk_api.VkApi(token=token)
        return vk.method("users.get", {"user_ids": user_id})
