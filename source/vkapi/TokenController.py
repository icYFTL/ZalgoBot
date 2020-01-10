from source.databases.InternalBD import InternalBD
from source.vkapi.UserAPI import UserAPI


class TokenController:
    def __init__(self, token):
        self.token = token
        self.ua = None

    def token_valid(self):
        return UserAPI.is_token_valid(self.token)

    def user_exists(self, user):
        return self.ua.user_exists(user)

    @staticmethod
    def token_exists(user_id):
        token = InternalBD.get_token(user_id)
        return token if token else False
