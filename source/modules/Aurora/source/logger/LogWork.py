import os

from source.modules.Aurora.source.static.StaticMethods import StaticMethods


class LogWork:
    template = "[{type}] ({time}): {event}"

    @staticmethod
    def init():
        try:
            os.mkdir("source/logger/logs/")
        except:
            pass

    @staticmethod
    def write(text):
        LogWork.init()
        f = open('source/logger/logs/log.txt', 'a', encoding='utf-8')
        f.write(text + '\n')
        f.close()

    @staticmethod
    def log(text):
        LogWork.write(LogWork.template.format(type='Log', time=StaticMethods.get_time().strftime("%D %T"), event=text))

    @staticmethod
    def warn(text):
        LogWork.write(
            LogWork.template.format(type='Warning', time=StaticMethods.get_time().strftime("%D %T"), event=text))

    @staticmethod
    def error(text):
        LogWork.write(
            LogWork.template.format(type='Error', time=StaticMethods.get_time().strftime("%D %T"), event=text))

    @staticmethod
    def fatal(text):
        LogWork.write(
            LogWork.template.format(type='Fatal', time=StaticMethods.get_time().strftime("%D %T"), event=text))
