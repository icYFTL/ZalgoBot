from threading import Thread

from source.main.Main import Main


class MessagesHandler(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            Main.handle()
