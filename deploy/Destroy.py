import json
from os import path, _exit, system

print('### DESTROY BEGIN ###')

if not path.exists('config.json'):
    print('Please run Destroy.py from root directory.')
    _exit(-1)

data: dict = json.load(open('config.json', 'r', encoding='UTF-8'))

system(f'sudo docker cp {data["docker_name"]}:/{data["db_name"]} ./')  # save db from docker container

# Destroy modules
for module in data['modules']:
    system(f'docker kill {module.lower()}')
    system(f'docker image rm {module.lower()} -f')
    system(f'docker rm {module.lower()}')

# Destroy main bot
system(f'docker kill {data["docker_name"]}')
system(f'docker image rm {data["docker_name"]} -f')
system(f'docker rm {data["docker_name"]}')

system('docker-compose rm -a')

data['modules'].clear()

open('config.json', 'w', encoding='UTF-8').write(json.dumps(data, ensure_ascii=False))

print('### ✅ DESTROY DONE ✅ ###')
