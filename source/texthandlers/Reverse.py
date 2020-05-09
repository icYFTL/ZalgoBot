class Reverse:
    @staticmethod
    def make(text: str) -> str:
        return text[::-1]

    def __repr__(self):
        return 'reverse'
