from source.ApiWorker import ApiWorker
from Config import Config


class ExitHandler(object):
    def bye():
        try:
            BA = ApiWorker()
            for admin in Config.admins:
                BA.message_send('Скрипт был аварийно остановлен.', admin, False)
        except:
            pass

        print('Shutting down...')
