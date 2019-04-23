import configparser
import os


class iniWorker:
    '''
    This class controls work with ini files.
    :return read_config -> [type, zalgo_type, zalgo_pos, messages_count]
    :return None
    '''

    @staticmethod
    def path_checker():
        try:
            os.mkdir('source/data/')
            return True
        except:
            return True

    @staticmethod
    def create_config(user_id):
        config = configparser.ConfigParser()
        config.add_section(str(user_id))
        config.set(str(user_id), "type", "zalgo")
        config.set(str(user_id), "zalgo_type", "average")
        config.set(str(user_id), "messages_count", "0")

        iniWorker.append_config(config)

    @staticmethod
    def change_config(user_id, key, value):
        config = configparser.ConfigParser()
        config.read('source/data/info.ini')
        config.set(str(user_id), key, value)
        iniWorker.write_config(config)

    @staticmethod
    def read_config(user_id):
        try:
            config = configparser.ConfigParser()
            config.read('source/data/info.ini')

            return {'type': config.get(str(user_id), "type"), 'zalgo_type': config.get(str(user_id), "zalgo_type"),
                    'messages_count': config.get(str(user_id), "messages_count")}
        except configparser.NoSectionError:
            return False

    @staticmethod
    def write_config(config):
        iniWorker.path_checker()
        with open('source/data/info.ini', "w") as config_file:
            config.write(config_file)

    @staticmethod
    def append_config(config):
        iniWorker.path_checker()
        with open('source/data/info.ini', "a") as config_file:
            config.write(config_file)

    @staticmethod
    def user_exists(user_id):
        if not iniWorker.read_config(user_id):
            return False
        return True
