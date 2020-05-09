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

# Deploy modules
for module in data['modules']:
    build = system(f'docker build -t {module.lower()} {path.join("source/modules/", module)}') == 0
    print(f"✅ {module} built successfully!") if build else print(f"🚫 {module} build failed")

    m_data: dict = json.load(open(path.join('source/modules/', module, 'Config.json'), 'r', encoding='UTF-8'))

    name = m_data['docker_name']
    host = m_data['web_server_host']
    port = m_data['web_server_port']

    deploy = system(f'docker run -p {port}:{port} -itd --name {name} --network="host" {name}') == 0

    print(f"✅ {module} deployed successfully!") if deploy else print(f"🚫 {module} deploy failed")

# Deploy main bot
name = data["docker_name"]
host = data["web_server_host"]
port = data["web_server_port"]

build = system(f'docker build -t {name.lower()} .') == 0
print(f"✅ Main bot built successfully!") if build else print(f"🚫 Main bot build failed")

deploy = system(f'docker run -p {port}:{port} -itd --name {name.lower()} --network="host" {name.lower()}') == 0
print(f"✅ Main bot deployed successfully!") if deploy else print(f"🚫 Main bot deploy failed")

print('### DEPLOY DONE ###')
