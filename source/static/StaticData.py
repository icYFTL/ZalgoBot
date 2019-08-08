import threading


class StaticData:
    name = 'ZalgoBot'
    version = '1.7.3 Alpha Release'
    author = 'icYFTL'
    stack_messages = []
    new_message_trigger = threading.Event()