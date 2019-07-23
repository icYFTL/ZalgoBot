import json

from flask import Flask
from flask import request

from source.other.StaticData import StaticData

zalgo_m = Flask(__name__)


@zalgo_m.route('/')
def hello_world():
    return 'Welcome to icYFTL\'s server.'


@zalgo_m.route('/', methods=['POST'])
def processing():
    # Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)
    # Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return "bb2072fc"
    elif data['type'] == 'message_new':
        StaticData.stack_messages.append({'message': data['object']['text'], 'user_id': data['object']['from_id']})
        StaticData.new_message_trigger()
        return 'ok'
