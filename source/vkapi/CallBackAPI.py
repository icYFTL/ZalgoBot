import json
import logging

import requests
from flask import Flask, request, redirect

from source.databases.InternalBD import InternalBD
from source.static.StaticData import StaticData
from source.vkapi.BotAPI import BotAPI
from Config import Config

m_thread = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@m_thread.route('/zalgo', methods=['GET'])
def get_access():
    try:
        code = request.args['code']
        access = json.loads(requests.get(
            f"https://oauth.vk.com/access_token?client_id=7112656&client_secret={Config.app_secret}&redirect_uri=https://icyftl.ru/zalgo&code=" + code).text)
        InternalBD.update_token(user_id=access['user_id'], token=access['access_token'])
        bot = BotAPI()
        bot.message_send('Access Token успешно зарегистрирован!', access['user_id'])
        return redirect("https://vk.com/im?sel=-181269537", code=302)
    except:
        return "Welcome to ZalgoBot server!"


@m_thread.route('/zalgo', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return Config.group_special_string
    elif data['type'] == 'message_new':
        if data['secret'] == Config.secret_key:
            payload = None
            if data['object'].get('payload'):
                payload = json.loads(data['object']['payload'])['button']
            StaticData.stack_messages.append({'message': data['object']['text'], 'user_id': data['object']['from_id'],
                                              'payload': payload})
            StaticData.new_message_trigger.set()
            return 'ok'
        else:
            return 'I actually don\'t like haCk3r$.', 418
