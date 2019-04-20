from source.BotApi import BotApi
from source.iniWorker import iniWorker

from Config import Config


class CommandsHandler:
    def __init__(self, user_id):
        self.botapi = BotApi(Config.access_token)
        self.user_id = user_id
        self.data = iniWorker.readConfig(self.user_id)

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
        elif comma == '/zalgo':
            self.zalgo_comma()
        elif comma == '/flip':
            self.flip_comma()
        elif comma == '/reverse':
            self.reverse_comma()
        else:
            self.undefined_comma()

    def help_comma(self):
        self.botapi.message_send('''
        Список команд:
        /options - Опции ZalgoText
        /stat - Текущие настройки ZalgoText
        /default - Вернуть стандартные настройки ZalgoBot
        /reverse - включить режим Reverse
        /flip - включить режим Flip
        /zalgo - включить режим Zalgo
        ''',
                                 self.user_id)

    def zalgo_comma(self):
        iniWorker.changeConfig(self.user_id, None, None, 'zalgo')
        self.botapi.message_send('Режим Zalgo активирован.',
                                 self.user_id)

    def flip_comma(self):
        iniWorker.changeConfig(self.user_id, None, None, 'flip')
        self.botapi.message_send('Режим Flip активирован.',
                                 self.user_id)

    def reverse_comma(self):
        iniWorker.changeConfig(self.user_id, None, None, 'reverse')
        self.botapi.message_send('Режим Reverse активирован.',
                                 self.user_id)

    def options_comma(self):
        print(self.data)
        if self.data[0] == 'zalgo':
            self.botapi.message_send(
                '''
                /zalgo_up - включить/выключить добавление Zalgo сверху символов
                /zalgo_mid - включить/выключить добавление Zalgo между символов
                /zalgo_down - включить/выключить добавление Zalgo снизу символов
                /zalgo_max - максимум Zalgo в тексте
                /zalgo_aver - средний уровень Zalgo в тексте
                /zalgo_min - минимум Zalgo в тексте
                ''', self.user_id)
        elif self.data[0] == 'flip':
            self.botapi.message_send(
                '''
                /reverse - включить режим Reverse
                /zalgo - включить режим Zalgo
                ''', self.user_id)
        elif self.data[0] == 'reverse':
            self.botapi.message_send(
                '''
                /flip - включить режим Flip
                /zalgo - включить режим Zalgo
                ''', self.user_id)

    def default_comma(self):
        iniWorker.changeConfig(self.user_id, 'average', '123', 'zalgo')
        self.botapi.message_send('Успешно изменено.', self.user_id)

    def stat_comma(self):
        print(self.data[0])
        if self.data[0] == 'zalgo':
            up = 'no'
            mid = 'no'
            down = 'no'
            if '1' in self.data[2]:
                up = 'yes'
            if '2' in self.data[2]:
                mid = 'yes'
            if '3' in self.data[2]:
                down = 'yes'

            self.botapi.message_send('''
            Режим: {}
            Размер Zalgo: {}
            Распространение Zalgo: 
            up   : {}
            mid  : {}
            down : {}
            '''.format(self.data[0], self.data[1], up, mid, down), self.user_id)
        elif self.data[0] == 'flip':
            self.botapi.message_send('''
            Режим: Flip
            ''', self.user_id)
        elif self.data[0] == 'reverse':
            self.botapi.message_send('''
                        Режим: Reverse
                        ''', self.user_id)

    def zalgo_up(self):
        if self.data[0] == 'zalgo':
            self.data = self.data[2]
            if self.data == 'None':
                self.data = ''
            if '1' in self.data:
                self.data = self.data.replace('1', '')
                self.botapi.message_send('Теперь Zalgo не будет наложена поверх символов.', self.user_id)
            else:
                self.data += '1'
                self.botapi.message_send('Теперь Zalgo будет наложена поверх символов.', self.user_id)
            if self.data == '':
                self.data = 'None'
            iniWorker.changeConfig(self.user_id, None, self.data, None)
        else:
            self.botapi.message_send('Активируйте режим Zalgo чтобы изменять настройки ZalgoText.', self.user_id)

    def zalgo_mid(self):
        if self.data[0] == 'zalgo':
            self.data = self.data[2]
            if self.data == 'None':
                self.data = ''
            if '2' in self.data:
                self.data = self.data.replace('2', '')
                self.botapi.message_send('Теперь Zalgo не будет наложена между символами.', self.user_id)
            else:
                self.data += '2'
                self.botapi.message_send('Теперь Zalgo будет наложена между символами.', self.user_id)
            if self.data == '':
                self.data = 'None'
            iniWorker.changeConfig(self.user_id, None, self.data, None)
        else:
            self.botapi.message_send('Активируйте режим Zalgo чтобы изменять настройки ZalgoText.', self.user_id)

    def zalgo_down(self):
        if self.data[0] == 'zalgo':
            self.data = self.data[2]
            if self.data == 'None':
                self.data = ''
            if '3' in self.data:
                self.data = self.data.replace('3', '')
                self.botapi.message_send('Теперь Zalgo не будет наложена под символами.', self.user_id)
            else:
                self.data += '3'
                self.botapi.message_send('Теперь Zalgo будет наложена под символами.', self.user_id)
            if self.data == '':
                self.data = 'None'
            iniWorker.changeConfig(self.user_id, None, self.data, None)
        else:
            self.botapi.message_send('Активируйте режим Zalgo чтобы изменять настройки ZalgoText.', self.user_id)

    def zalgo_max(self):
        if self.data[0] == 'zalgo':
            iniWorker.changeConfig(self.user_id, 'max', None, None)
            self.botapi.message_send('Теперь Zalgo  будет максимального размера.', self.user_id)
        else:
            self.botapi.message_send('Активируйте режим Zalgo чтобы изменять настройки ZalgoText.', self.user_id)

    def zalgo_aver(self):
        if self.data[0] == 'zalgo':
            iniWorker.changeConfig(self.user_id, 'average', None, None)
            self.botapi.message_send('Теперь Zalgo будет среднего размера.', self.user_id)
        else:
            self.botapi.message_send('Активируйте режим Zalgo чтобы изменять настройки ZalgoText.', self.user_id)

    def zalgo_min(self):
        if self.data[0] == 'zalgo':
            iniWorker.changeConfig(self.user_id, 'min', None, None)
            self.botapi.message_send('Теперь Zalgo будет минимального размера.', self.user_id)
        else:
            self.botapi.message_send('Активируйте режим Zalgo чтобы изменять настройки ZalgoText.', self.user_id)

    def undefined_comma(self):
        self.botapi.message_send('Нет такой команды.', self.user_id)
