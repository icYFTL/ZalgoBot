import threading


class StaticData:
    name = 'ZalgoBot'
    version = '2.2.1'
    author = 'icYFTL'

    stack_messages = []
    new_message_trigger = threading.Event()
