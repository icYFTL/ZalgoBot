class Cout:
    @staticmethod
    def make(text: str) -> str:
        return ''.join(['&#0822;' + x for x in text])

    def __repr__(self):
        return 'cout'
