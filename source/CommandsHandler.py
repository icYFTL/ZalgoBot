from source.BotApi import BotApi
from source.iniWorker import iniWorker

from Config import Config


class CommandsHandler:
    def __init__(self, user_id):
        self.botapi = BotApi(Config.access_token)
        self.user_id = user_id

    def identify_comma(self, comma):
        if comma == '/help':
            self.help_comma()
        elif comma == '/options':
            self.options_comma()
        elif comma == '/stat':
            self.stat_comma()
        elif comma == '/default':
            self.default_comma()
        elif comma == '/zalgo_up':
            self.zalgo_up()
        elif comma == '/zalgo_mid':
            self.zalgo_mid()
        elif comma == '/zalgo_down':
            self.zalgo_down()
        elif comma == '/zalgo_max':
            self.zalgo_max()
        elif comma == '/zalgo_aver':
            self.zalgo_aver()
        elif comma == '/zalgo_min':
            self.zalgo_min()
        else:
            self.undefined_comma()

    def help_comma(self):
        self.botapi.message_send('''
        Список команд:
        /options - Опции ZalgoBot
        /stat - Текущие настройки ZalgoBot
        /default - Вернуть стандартные настройки ZalgoBot
        ''',
                                 self.user_id, False)

    def options_comma(self):
        self.botapi.message_send(
            '''
            /zalgo_up - включить/выключить добавление Zalgo сверху символов
            /zalgo_mid - включить/выключить добавление Zalgo между символов
            /zalgo_down - включить/выключить добавление Zalgo снизу символов
            /zalgo_max - максимум Zalgo в тексте
            /zalgo_aver - средний уровень Zalgo в тексте
            /zalgo_min - минимум Zalgo в тексте
            ''', self.user_id, False)

    def default_comma(self):
        iniWorker.changeConfig(self.user_id, 'average', '123')
        self.botapi.message_send('Успешно изменено.', self.user_id, False)

    def stat_comma(self):
        data = iniWorker.readConfig(self.user_id)
        up = 'no'
        mid = 'no'
        down = 'no'
        if '1' in data[1]:
            up = 'yes'
        if '2' in data[1]:
            mid = 'yes'
        if '3' in data[1]:
            down = 'yes'

        self.botapi.message_send('''
        Размер Zalgo: {}
        Распространение Zalgo: 
        up   : {}
        mid  : {}
        down : {}
        '''.format(data[0], up, mid, down), self.user_id, False)

    def zalgo_up(self):
        data = str(iniWorker.readConfig(self.user_id)[1])
        if data == 'None':
            data = ''
        if '1' in data:
            data = data.replace('1', '')
            self.botapi.message_send('Теперь Zalgo не будет наложена поверх символов.', self.user_id, False)
        else:
            data += '1'
            self.botapi.message_send('Теперь Zalgo будет наложена поверх символов.', self.user_id, False)
        if data == '':
            data = 'None'
        iniWorker.changeConfig(self.user_id, None, data)

    def zalgo_mid(self):
        data = str(iniWorker.readConfig(self.user_id)[1])
        if data == 'None':
            data = ''
        if '2' in data:
            data = data.replace('2', '')
            self.botapi.message_send('Теперь Zalgo не будет наложена между символами.', self.user_id, False)
        else:
            data += '2'
            self.botapi.message_send('Теперь Zalgo будет наложена между символами.', self.user_id, False)
        if data == '':
            data = 'None'
        iniWorker.changeConfig(self.user_id, None, data)

    def zalgo_down(self):
        data = str(iniWorker.readConfig(self.user_id)[1])
        if data == 'None':
            data = ''
        if '3' in data:
            data = data.replace('3', '')
            self.botapi.message_send('Теперь Zalgo не будет наложена под символами.', self.user_id, False)
        else:
            data += '3'
            self.botapi.message_send('Теперь Zalgo будет наложена под символами.', self.user_id, False)
        if data == '':
            data = 'None'
        iniWorker.changeConfig(self.user_id, None, data)

    def zalgo_max(self):
        iniWorker.changeConfig(self.user_id, 'max', None)
        self.botapi.message_send('Теперь Zalgo  будет максимального размера.', self.user_id, False)

    def zalgo_aver(self):
        iniWorker.changeConfig(self.user_id, 'average', None)
        self.botapi.message_send('Теперь Zalgo будет среднего размера.', self.user_id, False)

    def zalgo_min(self):
        iniWorker.changeConfig(self.user_id, 'min', None)
        self.botapi.message_send('Теперь Zalgo будет минимального размера.', self.user_id, False)

    def undefined_comma(self):
        self.botapi.message_send('Нет такой команды. Используйте /help для получения списка комманд.', self.user_id,
                                 False)
