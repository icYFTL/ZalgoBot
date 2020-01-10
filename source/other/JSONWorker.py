class JSONWorker:
    '''
    This class controls work with JSON.
    :return read_json -> keyboard.json
    '''

    @staticmethod
    def read_json(file) -> str:
        return open("source/interfaces/keyboards/{}.json".format(file), "r", encoding="UTF-8").read()
