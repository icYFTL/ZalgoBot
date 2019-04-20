import configparser
import os


class iniWorker:
    @staticmethod
    def path_checker():
        try:
            os.mkdir('source/data/')
            return True
        except:
            return True

    @staticmethod
    def createConfig(user_id):
        config = configparser.ConfigParser()
        config.add_section(str(user_id))
        config.set(str(user_id), "type", "zalgo")
        config.set(str(user_id), "zalgo_type", "average")
        config.set(str(user_id), "zalgo_pos", "123")

        iniWorker.writeConfig(config)

    @staticmethod
    def changeConfig(user_id, zalgotype, zalgopos, type):
        config = configparser.ConfigParser()
        config.read('source/data/info.ini')

        if type:
            config.set(str(user_id), "type", type)
        if zalgotype:
            config.set(str(user_id), "zalgo_type", zalgotype)
        if zalgopos:
            config.set(str(user_id), "zalgo_pos", zalgopos)

        iniWorker.writeConfig(config)

    @staticmethod
    def readConfig(user_id):
        try:
            config = configparser.ConfigParser()
            config.read('source/data/info.ini')

            type = config.get(str(user_id), "type")
            zalgo_type = config.get(str(user_id), "zalgo_type")
            zalgo_pos = config.get(str(user_id), "zalgo_pos")

            return [type, zalgo_type, zalgo_pos]
        except configparser.NoSectionError:
            return False

    @staticmethod
    def writeConfig(config):
        iniWorker.path_checker()
        with open('source/data/info.ini', "w") as config_file:
            config.write(config_file)

    @staticmethod
    def user_exists(user_id):
        if not iniWorker.readConfig(user_id):
            return False
        return True
