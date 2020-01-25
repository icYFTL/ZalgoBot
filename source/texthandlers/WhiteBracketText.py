class WhiteBracketText:
    @staticmethod
    def white_bracket(income) -> str:
        _temp = ''
        for i in income:
            _temp += f'『{i}』'
        return _temp
