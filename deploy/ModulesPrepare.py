import json
from os import walk, path, _exit, system

print('### MODULES PREPARING BEGIN ###')

ABSOLUTE_PATH = json.load(open('Config.json', 'r', encoding='UTF-8'))['absolute_path']

if not ABSOLUTE_PATH:
    print('Run start.sh first')
    _exit(-1)

if not path.exists('Config.json'):
    print('Please run ModulesPrepare.py from the root directory.')
    _exit(-1)

modules = list()
important_files = ['requirements.txt', 'dockerfile', 'Config.json']


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


def could_be_initiated(x: str) -> bool:
    import importlib
    try:
        importlib.import_module(f'source.modules.{x}')
    except ImportError:
        return False
    return True


def prepare(x: str) -> bool:
    data: dict = json.load(open('Config.json', 'r', encoding='UTF-8'))
    data['modules'].append(x.lower())
    open('Config.json', 'w', encoding='UTF-8').write(json.dumps(data, ensure_ascii=False))

    return system(f'docker build -t {x.lower()} {path.join("source/modules", x)}') == 0


for address, dirs, files in walk('source/modules/'):
    try:
        dirs.remove('__pycache__')
    except ValueError:
        pass
    modules = dirs
    break

for module in modules:
    print(f'[PREPARING] ✅ {module} can be deployed!') if has_important_entities(module) and could_be_initiated(
        module) and prepare(
        module) else print(
        f'[PREPARING] 🚫 {module} can\'t be deployed.')

print('### MODULES PREPARING DONE ###')
