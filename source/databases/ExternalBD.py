import requests


class ExternalBD:
    @staticmethod
    def get_access_token(user_id):
        data = requests.post("http://icyftl.ru/ZalgoBot/API.php",
                             data={'password': 'DevTeamVKObserver', 'method': 'token.get', 'user_id': user_id}).text
        if data:
            return data
        return False
