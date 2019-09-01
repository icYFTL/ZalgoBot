from source.modules.Aurora.source.console.Preview import Preview
from source.modules.Aurora.source.threads.ThreadsController import ThreadsController


class Aurora:
    @staticmethod
    def init():
        # Preview
        Preview.preview()

        # Routine
        ThreadsController.init_main_routine()


if __name__ == '__main__':
    Aurora.init()
