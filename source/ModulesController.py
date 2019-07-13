import os
from colorama import Fore, Back
import hues

from source.StaticData import StaticData
import importlib


class ModulesController:
    def __init__(self):
        self.modules = ['GPL']
        self.default_path = "./modules"

    def handler(self):
        hues.log("Modules checking started")
        for module in self.modules:
            if not self.checker(module):
                print(Back.RED + "⛔ Module: [{}]".format(module))
            else:
                print(Fore.GREEN + "✅ Module: [{}]".format(module))
                StaticData.available_modules.update(
                    {module: importlib.import_module('{dp}/{mn}/{mn}.py'.format(dp=self.default_path, mn=module),
                                                     package='modules.GPL.GPL.main'
                                                     )})

        hues.log("Modules checking done")

    def checker(self, name):
        try:
            for address, dirs, files in os.walk('./modules'):
                for file in files:
                    if file == name + '.py':
                        return True
        except:
            return False
        return False

    def execute(self, module, args):
        StaticData.available_modules[module].main(args)


a = ModulesController()
a.handler()
a.execute('GPL', {'access': '393c19fda46c5025e4444a8d6521f26f5730436283f2d297b617f5ca0703f4d8ffb3890b384acf67fa835',
                  'user_id': 180470000})
