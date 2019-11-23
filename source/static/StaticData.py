import threading


class StaticData:
    name = 'ZalgoBot'
    version = '1.9.5'
    author = 'icYFTL'
    stack_messages = []
    new_message_trigger = threading.Event()
