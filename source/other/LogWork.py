import logging

import hues


class LogWork:
    @staticmethod
    def base_init():
        logging.basicConfig(filename="default.log", level=logging.INFO)

    @staticmethod
    def log(message):
        logging.info(message)
        hues.log(message)

    @staticmethod
    def warn(message):
        logging.warning(message)
        hues.warn(message)

    @staticmethod
    def error(message):
        logging.error(message)
        hues.error(message)

    @staticmethod
    def fatal(message):
        logging.fatal(message)
        hues.error("Fatal: " + message)
