import json


def keyboard_handler(filename: str) -> json:
    data = json.loads(open(f'source/interfaces/keyboards/{filename}.json', 'r', encoding='UTF-8').read())
    if filename != 'default':
        data['buttons'].append(
            json.loads(open('source/interfaces/keyboards/back.json', 'r', encoding='UTF-8').read()))
    return json.dumps(data)


def message_handler(msg: str, lang='ru', location='config.json') -> str:
    if location == 'config.json':
        from core import config
        return config.get(f'msg_{lang}', {}).get(msg)
    return json.load(open(location, 'r', encoding='UTF-8')).get(f'msg_{lang}', {}).get(msg)
