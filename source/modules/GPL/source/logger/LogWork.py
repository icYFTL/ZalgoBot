import os

import hues
from source.static.StaticMethods import StaticMethods


class LogWork:
    template = "[{type}] ({time}): {event}"

    @staticmethod
    def init():
        return
        try:
            os.mkdir("source/logger/logs/")
        except:
            pass

    @staticmethod
    def write(text):
        return
        LogWork.init()
        f = open('source/logger/logs/zalgo_log.log', 'a', encoding='utf-8')
        f.write(text + '\n')
        f.close()

    @staticmethod
    def log(text):
        return
        hues.log(text)
        LogWork.write(LogWork.template.format(type='Log', time=StaticMethods.get_time().strftime("%D %T"), event=text))

    @staticmethod
    def warn(text):
        return
        hues.warn(text)
        LogWork.write(
            LogWork.template.format(type='Warning', time=StaticMethods.get_time().strftime("%D %T"), event=text))

    @staticmethod
    def error(text):
        return
        hues.error(text)
        LogWork.write(
            LogWork.template.format(type='Error', time=StaticMethods.get_time().strftime("%D %T"), event=text))

    @staticmethod
    def fatal(text):
        return
        hues.error("FATAL: " + text)
        LogWork.write(
            LogWork.template.format(type='Fatal', time=StaticMethods.get_time().strftime("%D %T"), event=text))

    @staticmethod
    def success(text):
        return
        hues.success(text)
        LogWork.write(
            LogWork.template.format(type='Success', time=StaticMethods.get_time().strftime("%D %T"), event=text))
