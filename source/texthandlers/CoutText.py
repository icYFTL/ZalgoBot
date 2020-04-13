class CoutTextMaker:
    @staticmethod
    def make(text: str) -> str:
        return ''.join(['&#0822;' + x for x in text])
