import sys
import time
from source.ConsoleWorker import ConsoleWorker
from source.StaticData import StaticData
import hues


class Preview:
    '''
    This class controls showing preview on the start of the script
    :return None
    '''

    @staticmethod
    def preview():
        ConsoleWorker.clear_console()
        print('[{}] v{} Alpha Release'.format(StaticData.name, StaticData.version))
        author = 'by icYFTL\n\n'

        notice = "If you got error or something else: write me\nTelegram: @icYFTL\nDarkWeb: Denuvo"

        for i in range(len(author)):
            if author[i].isalpha() or author[i - 1].isalpha() and i != 0:
                sys.stdout.write(author[i])
                sys.stdout.flush()
                time.sleep(0.2)
            else:
                sys.stdout.write(author[i])
                sys.stdout.flush()
        hues.warn(notice)
        print('\n\n\n')
