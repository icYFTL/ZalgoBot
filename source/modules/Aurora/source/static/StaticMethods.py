from datetime import datetime

import pytz


class StaticMethods:
    @staticmethod
    def get_time():
        return datetime.now(pytz.timezone('Europe/Moscow'))
