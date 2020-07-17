import json
from os import walk, path, _exit

config = json.load(open('config.json', 'r', encoding='UTF-8'))

if not config['use_modules']:
    print('### ⚠ MODULES DISABLED ⚠ ###')
    _exit(0)

print('### MODULES PREPARING BEGIN ###')

if not config['absolute_path']:
    print('Run start.sh first')
    _exit(-1)

if not path.exists('config.json'):
    print('Please run ModulesPrepare.py from the root directory.')
    _exit(-1)

if not config['modules']:
    print('### ⚠ NO ONE MODULE IN CONFIG ⚠ ###')
    _exit(-1)

modules = list()
important_files = ['requirements.txt', 'dockerfile', 'config.json']


def has_important_entities(x: str) -> bool:
    check_done: bool = True
    executable = f'{x}.py'

    important_files.append(executable)

    x = path.join('source/modules/', x)
    for entity in important_files:
        if not path.exists(path.join(x, entity)):
            print(f'🚫 {entity} isn\'t exists in module {x}')
            check_done = False

    important_files.remove(executable)

    return check_done


for address, dirs, files in walk('source/modules/'):
    try:
        dirs.remove('__pycache__')
    except ValueError:
        pass
    modules = dirs
    break

for module in modules:
    print(f'[PREPARING] ✅ {module} can be deployed!') if has_important_entities(module) else print(
        f'[PREPARING] 🚫 {module} can\'t be deployed.')

print('### ✅ MODULES PREPARING DONE ✅ ###')
