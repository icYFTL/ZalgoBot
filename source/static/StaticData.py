import threading


class StaticData:
    name = 'ZalgoBot'
    version = '3.1.0.0 Alpha'
    author = 'icYFTL'

    stack_messages = []
    new_message_trigger = threading.Event()
