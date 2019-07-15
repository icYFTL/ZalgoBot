import os


def module_add(name):
    files_s = []
    for address, dirs, files in os.walk('./{name}/source/'.format(name=name)):
        for file in files:
            files_s.append(file)
    for file in files_s:
        f = open('./{name}/source/{file}'.format(name=name, file=file), 'r', encoding='utf-8')
        data = f.read()
        f.close()
        pass


module_add("GPL")
