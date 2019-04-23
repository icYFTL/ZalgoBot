class JSONWorker:
    '''
    This class controls work with JSON.
    :return read_json -> keyboard.json
    '''

    @staticmethod
    def read_json(file):
        return open("source/keyboards/{}".format(file), "r", encoding="UTF-8").read()
