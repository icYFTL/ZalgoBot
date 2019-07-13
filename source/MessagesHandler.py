from threading import Thread
from source.Main import Main


class MessagesHandler(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            handler = Main()
            handler.handle()
