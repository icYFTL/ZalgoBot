import json


def keyboard_handler(filename: str) -> json:
    data = json.loads(open(f'source/interfaces/keyboards/{filename}.json', 'r', encoding='UTF-8').read())
    if filename != 'default':
        data['buttons'].append(
            json.loads(open('source/interfaces/keyboards/back.json', 'r', encoding='UTF-8').read()))
    return json.dumps(data)


def message_handler(msg: str, lang='ru', location='Config.json') -> str:
    return json.load(open(location, 'r', encoding='UTF-8')).get(f'msg_{lang}', {}).get(msg)
