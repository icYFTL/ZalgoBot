import json
import logging

import requests
from flask import Flask, request, redirect

from Static.StaticData import StaticData
from source.databases.InternalBD import InternalBD

m_thread = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@m_thread.route('/', methods=['GET'])
def get_access():
    try:
        code = request.args['code']
        access = json.loads(requests.get(
            "https://oauth.vk.com/access_token?client_id=6949573&client_secret=yTy9ne0P6B0MmzZLDLPr&redirect_uri=http://http://195.133.144.12/&code=" + code).text)
        InternalBD.add_token(user_id=access['user_id'], token=access['access_token'])
        return redirect("https://vk.com/im?sel=-181269537", code=302)
    except:
        return "Welcome to ZalgoBot server!"


@m_thread.route('/', methods=['POST'])
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
        StaticData.new_message_trigger.set()
        return 'ok'
