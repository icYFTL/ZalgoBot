import threading


class StaticData:
    name = 'ZalgoBot'
    version = '1.6.1 Alpha Release'
    author = 'icYFTL'
    stack_messages = []
    new_message_trigger = threading.Event()
    reboot_env = None
