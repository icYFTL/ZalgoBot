import json
from os import system, path, _exit

print('### DEPLOY BEGIN ###')

if not path.exists('config.json'):
    print('Please run Deploy.py from root directory.')
    _exit(-1)

# Get config.json
config: dict = json.load(open('config.json', 'r', encoding='UTF-8'))

params_ok: bool = True
important_keys = 'docker_name', 'web_server_host', 'web_server_port', \
                 'db_name', 'admins', 'access_token', \
                 'group_id', 'group_special_string', 'app_secret'

# Params check
if not config['no_checks']:
    for x in list(config):
        if not config[x] and x in important_keys:
            print(f'Parameter unfilled: {x}')
            params_ok = False

if not params_ok:
    _exit(-1)

if system(f'docker-compose build --force_recreate') == 0:
    print('✅ Build success!')
else:
    print('🚫 Build failed.')
    _exit(-1)

if system(f'docker-compose up -d') == 0:
    print('✅ Up done!')
else:
    print('🚫 Up failed.')
    _exit(-1)

print('### ✅ DEPLOY DONE ✅ ###')
