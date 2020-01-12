import json


class JSONWorker:
    '''
    This class controls work with JSON.
    :return keyboard_handler -> {keyboard}.json
    '''

    @staticmethod
    def keyboard_handler(file) -> json:
        return json.loads(open(f'source/interfaces/keyboards/{file}.json', 'r', encoding='UTF-8').read())[
            'buttons'].append(json.loads(open('source/interfaces/keyboards/back.json', 'r', encoding='UTF-8').read()))
