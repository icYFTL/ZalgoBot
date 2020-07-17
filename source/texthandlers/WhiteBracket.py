class WhiteBracket:
    @staticmethod
    def make(text: str, mode=1) -> str:
        if mode == 0:
            text = text.split()
        elif mode == 1:
            pass
        return ''.join([f'『{x}』' for x in text if x != ' '])

    def __repr__(self):
        return 'white_bracket'