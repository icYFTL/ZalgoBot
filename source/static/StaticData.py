import threading


class StaticData:
    name = 'ZalgoBot'
    version = '1.9.8'
    author = 'icYFTL'
    stack_messages = []
    new_message_trigger = threading.Event()
