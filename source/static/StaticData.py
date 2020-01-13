import threading


class StaticData:
    name = 'ZalgoBot'
    version = '2.0.3'
    author = 'icYFTL'
    stack_messages = []
    new_message_trigger = threading.Event()
