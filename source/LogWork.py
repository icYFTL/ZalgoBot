import logging

import hues


class LogWork:
    @staticmethod
    def base_init():
        logging.basicConfig(filename="default.log", level=logging.INFO)

    @staticmethod
    def add_note(kind, message):
        LogWork.base_init()
        if kind == 'info':
            logging.info(message)
            hues.log(message)
        elif kind == 'warning':
            logging.warning(message)
            hues.warn(message)
        elif kind == 'error':
            logging.error(message)
            hues.error(message)
        elif kind == 'fatal':
            logging.fatal(message)
            hues.error(message)
