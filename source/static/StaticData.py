import threading


class StaticData:
    name = 'ZalgoBot'
    version = '3.0.1.0 EXP'
    author = 'icYFTL'

    stack_messages = []
    new_message_trigger = threading.Event()
