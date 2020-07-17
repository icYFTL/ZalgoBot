import json
import os
import subprocess

print('### UPDATE BEGIN ###')

enable_updates = lambda x: open('config.json', 'w', encoding='UTF-8').write(json.dumps({'enable_updates': x}))

if not os.path.exists('ZalgoBot.py'):
    print('Please run Update.py from root directory.')
    os._exit(-1)

conf = None
try:
    with open('config.json', 'r', encoding='UTF-8') as f:
        conf = json.loads(f.read())

    if conf['enable_updates'] == "0":
        os._exit(-1)

    if os.system('git --version > /dev/null 2>&1') != 0:
        raise SystemError

    latest_head = \
        subprocess.Popen('git ls-remote origin refs/heads/master'.split(), stdout=subprocess.PIPE).communicate()[
            0].decode()[:40]
    current_head = subprocess.Popen('git rev-parse HEAD'.split(), stdout=subprocess.PIPE).communicate()[0].decode()[:40]

    if latest_head != current_head:
        print('Update available!\nDownload?(y/n)')
        ans = input('> ')
        while ans.lower() not in ['y', 'n']:
            ans = input('> ')

        if ans == 'y':
            os.system('git pull')

        from source.static.StaticData import StaticData

        print(f'Updated.\nCurrent version is {StaticData.version}')

    else:
        print('Up to date!')
        os._exit(0)


except FileNotFoundError:
    print('Update failed.\nConfig json not found.')
except json.JSONDecodeError:
    print('Update failed.\nIncorrect json.')
except SystemError:
    print('Update failed.\nGit not found.')
except:
    print('Update failed.')

enable_updates("0")

print('### UPDATE DONE ###')
