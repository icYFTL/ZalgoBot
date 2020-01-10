import os
import sys
import time

from source.static.StaticData import StaticData


class Preview:
    @staticmethod
    def preview():
        if os.system('clear') != 0:
            os.system('cls')
        print(f'[{StaticData.name}] v{StaticData.version}')
        corp = f'by {StaticData.author}\n\n'

        for i in range(len(corp)):
            if corp[i].isalpha() or corp[i - 1].isalpha() and i != 0:
                sys.stdout.write(corp[i])
                sys.stdout.flush()
                time.sleep(0.2)
            else:
                sys.stdout.write(corp[i])
                sys.stdout.flush()
