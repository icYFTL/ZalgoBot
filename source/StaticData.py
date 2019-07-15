import threading


class StaticData:
    name = 'ZalgoBot'
    version = '1.5 Alpha Release'
    author = 'icYFTL'
    stack_messages = []
    stack_waiters = []
    stack_module_repls = []
    trigger = threading.Event()
