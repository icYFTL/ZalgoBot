import json
from os import system, path, _exit

print('### DEPLOY BEGIN ###')

if not path.exists('Config.json'):
    print('Please run Deploy.py from root directory.')
    _exit(-1)

# Get Config.json
data: dict = json.load(open('Config.json', 'r', encoding='UTF-8'))

params_ok: bool = True
important_keys = 'docker_name', 'web_server_host', 'web_server_port', \
                 'db_name', 'admins', 'access_token', \
                 'group_id', 'group_special_string', 'app_secret', 'modules_path'

# Params check
for x in list(data):
    if not data[x]:
        print(f'Parameter unfilled: {x}')
        params_ok = False

if not params_ok:
    _exit(-1)


if system(f'docker-compose build') == 0:
    print('✅ Build success!')
else:
    print('🚫 Build failed.')

if system(f'docker-compose up') == 0:
    print('✅ Up done!')
else:
    print('🚫 Up failed.')


print('### DEPLOY DONE ###')
