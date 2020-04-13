class WhiteBracketText:
    @staticmethod
    def make(text: str) -> str:
        return ''.join([f'『{x}』' for x in text])
