class WhiteBracket:
    @staticmethod
    def make(text: str) -> str:
        return ''.join([f'『{x}』' for x in text])

    def __repr__(self):
        return 'white_bracket'
