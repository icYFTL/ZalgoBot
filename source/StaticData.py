import threading


class StaticData:
    name = 'ZalgoBot'
    version = '1.4 Alpha Release'
    author = 'icYFTL'
    stack = []
    trigger = threading.Event()
    available_modules = {}
