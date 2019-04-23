from source.BotApi import BotApi
from source.iniWorker import iniWorker
from source.JSONWorker import JSONWorker

from Config import Config


class CommandsHandler:
    '''
    This class controls commands handling.
    :param user_id
    :param identify_comma -> comma
    :return None
    '''

    def __init__(self, user_id):
        self.botapi = BotApi(Config.access_token)
        self.user_id = user_id
        self.data = iniWorker.read_config(self.user_id)

    def identify_comma(self, comma):
        if comma == '/help':
            self.help_comma()
        elif comma == '/options':
            self.options_comma()
        elif comma == '/stat':
            self.stat_comma()
        elif comma == '/default':
            self.default_comma()
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
        elif comma == '/change_mode':
            self.change_mode_comma()
        elif comma == '/back':
            self.back_comma()
        else:
            self.undefined_comma()

    def back_comma(self):
        mode = self.data.get('type')
        if mode == 'zalgo':
            self.botapi.message_send('Отменено', self.user_id, JSONWorker.read_json('zalgokey.json'))
        elif mode == 'flip':
            self.botapi.message_send('Отменено', self.user_id, JSONWorker.read_json('flipkey.json'))
        elif mode == 'reverse':
            self.botapi.message_send('Отменено', self.user_id, JSONWorker.read_json('reversekey.json'))

    def change_mode_comma(self):
        self.botapi.message_send('''
                Выберите режим:
                /reverse - Включить режим Reverse
                /flip - Включить режим Flip
                /zalgo - Включить режим Zalgo
                ''',
                                 self.user_id, JSONWorker.read_json('3way.json'))

    def help_comma(self):
        mode = self.data.get('type')
        if mode == 'zalgo':
            self.botapi.message_send('''
            Список команд:
            /options - Опции ZalgoText
            /stat - Текущие настройки ZalgoText
            /default - Вернуть стандартные настройки
            /change_mode - Сменить режим
            ''',
                                     self.user_id, JSONWorker.read_json('zalgokey.json'))
        elif mode == 'flip':
            self.botapi.message_send('''
                        Список команд:
                        /default - Вернуть стандартные настройки
                        /change_mode - Сменить режим
                        ''',
                                     self.user_id, JSONWorker.read_json('flipkey.json'))
        elif mode == 'reverse':
            self.botapi.message_send('''
                                    Список команд:
                                    /default - Вернуть стандартные настройки
                                    /change_mode - Сменить режим
                                    ''',
                                     self.user_id, JSONWorker.read_json('reversekey.json'))

    def zalgo_comma(self):
        iniWorker.change_config(self.user_id, 'type', 'zalgo')
        self.botapi.message_send('Режим Zalgo активирован.',
                                 self.user_id, JSONWorker.read_json('zalgokey.json'))

    def flip_comma(self):
        iniWorker.change_config(self.user_id, 'type', 'flip')
        self.botapi.message_send('Режим Flip активирован.',
                                 self.user_id, JSONWorker.read_json('flipkey.json'))

    def reverse_comma(self):
        iniWorker.change_config(self.user_id, 'type', 'reverse')
        self.botapi.message_send('Режим Reverse активирован.',
                                 self.user_id, JSONWorker.read_json('reversekey.json'))

    def options_comma(self):
        mode = self.data.get('type')
        if mode == 'zalgo':
            self.botapi.message_send(
                '''
                /zalgo_max - максимум Zalgo в тексте
                /zalgo_aver - средний уровень Zalgo в тексте
                /zalgo_min - минимум Zalgo в тексте
                ''', self.user_id, JSONWorker.read_json('zalgooptions.json'))
        elif mode == 'flip':
            self.botapi.message_send(
                '''
                /default - Вернуть стандартные настройки
                        /change_mode - Сменить режим
                ''', self.user_id, JSONWorker.read_json('flipkey.json'))
        elif mode == 'reverse':
            self.botapi.message_send(
                '''
                /default - Вернуть стандартные настройки
                        /change_mode - Сменить режим
                ''', self.user_id, JSONWorker.read_json('reversekey.json'))

    def default_comma(self):
        iniWorker.change_config(self.user_id, 'type', 'zalgo')
        iniWorker.change_config(self.user_id, 'zalgo_type', 'average')
        self.botapi.message_send('Успешно изменено.', self.user_id, JSONWorker.read_json('zalgokey.json'))

    def stat_comma(self):
        mode = self.data.get('type')
        if mode == 'zalgo':
            self.botapi.message_send('''
            Режим: {}
            Размер Zalgo: {}
            Всего сообщений обработано: {}
            '''.format(self.data.get('type'), self.data.get('zalgo_type'), str(self.data.get('messages_count'))),
                                     self.user_id, JSONWorker.read_json('zalgokey.json'))

        elif mode == 'flip':
            self.botapi.message_send('''
            Режим: Flip
            ''', self.user_id, JSONWorker.read_json('flipkey.json'))
        elif mode == 'reverse':
            self.botapi.message_send('''
                        Режим: Reverse
                        ''', self.user_id, JSONWorker.read_json('reversekey.json'))

    def zalgo_max(self):
        if self.data.get('type') == 'zalgo':
            iniWorker.change_config(self.user_id, 'zalgo_type', 'max')
            self.botapi.message_send('Теперь Zalgo  будет максимального размера.', self.user_id,
                                     JSONWorker.read_json('zalgokey.json'))
        else:
            self.botapi.message_send('Активируйте режим Zalgo чтобы изменять настройки ZalgoText.', self.user_id, None)

    def zalgo_aver(self):
        if self.data.get('type') == 'zalgo':
            iniWorker.change_config(self.user_id, 'zalgo_type', 'average')
            self.botapi.message_send('Теперь Zalgo будет среднего размера.', self.user_id,
                                     JSONWorker.read_json('zalgokey.json'))
        else:
            self.botapi.message_send('Активируйте режим Zalgo чтобы изменять настройки ZalgoText.', self.user_id, None)

    def zalgo_min(self):
        if self.data.get('type') == 'zalgo':
            iniWorker.change_config(self.user_id, 'zalgo_type', 'min')
            self.botapi.message_send('Теперь Zalgo будет минимального размера.', self.user_id,
                                     JSONWorker.read_json('zalgokey.json'))
        else:
            self.botapi.message_send('Активируйте режим Zalgo чтобы изменять настройки ZalgoText.', self.user_id, None)

    def undefined_comma(self):
        self.botapi.message_send('Нет такой команды.', self.user_id, None)
