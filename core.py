import json
import logging

logging.basicConfig(filename='zalgo_log.log', level=logging.INFO,
                    format='%(asctime)-15s | [%(name)s] %(levelname)s => %(message)s')
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

config: dict = json.load(open('config.json', 'r', encoding='UTF-8'))
