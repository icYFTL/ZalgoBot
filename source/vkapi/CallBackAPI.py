import json
import logging
import re
from flask import Flask, request, render_template

from source.databases.InternalBD import InternalBD
from source.static.StaticData import StaticData
from source.vkapi.BotAPI import BotAPI
from Config import Config

m_thread = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@m_thread.route('/zalgo', methods=['GET'])
def get_access():
    # try:
    #     code = request.args['code']
    #     access = json.loads(requests.get(
    #         f"https://oauth.vk.com/access_token?client_id=7112656&client_secret={Config.app_secret}&redirect_uri=https://icyftl.ru/zalgo&code=" + code).text)
    #     InternalBD.update_token(user_id=access['user_id'], token=access['access_token'])
    #     bot = BotAPI()
    #     bot.message_send('Access Token успешно зарегистрирован!', access['user_id'])
    #     return redirect("https://vk.com/im?sel=-181269537", code=302)
    # except:
    return render_template('index.html')


@m_thread.route('/zalgo', methods=['POST'])
def processing():
    try:
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
                StaticData.stack_messages.append(
                    {'message': data['object']['text'], 'user_id': data['object']['from_id'],
                     'payload': payload})
                StaticData.new_message_trigger.set()
                return 'ok'
            else:
                raise BaseException
        elif data['type'] == 'access_implementing':
            access = {}
            bot = BotAPI()
            if 'access_token' in data['data']:
                data = re.sub(r'(http)?https?:\/\/.*[#]', '', data['data'])
                for i in data.split('&'):
                    access[i.split('=')[0]] = i.split('=')[1]

                if re.match(r'[a-z0-9]{85}', access['access_token']) and int(access['user_id']):
                    InternalBD.update_token(user_id=access['user_id'], token=access['access_token'])
                    bot.message_send('Access Token успешно зарегистрирован!', access['user_id'])
                    return 'ok', 200
            if access.get('user_id'):
                bot.message_send(
                    'При регистрации Access Token произошла ошибка!\nПопробуйте еще раз или обратитесь к администратору сообщества.',
                    user_id=access['user_id'])
            return 'Something went wrong', 500

    except:
        return 'I actually don\'t like haCk3r$.', 418
