class CoutTextMaker:
    @staticmethod
    def cout(text) -> str:
        newstr = ''
        for i in text:
            newstr += '&#0822;' + i
        return newstr
