class FlipTextMaker:
    '''
    This class controls making flip decoration of text.
    :return flip -> flipped text
    '''
    flipTable = {
        'a': '\u0250',
        'b': 'q',
        'c': '\u0254',
        'd': 'p',
        'e': '\u01DD',
        'f': '\u025F',
        'g': '\u0183',
        'h': '\u0265',
        'i': '\u0131',
        'j': '\u027E',
        'k': '\u029E',
        'l': '\u0283',
        'm': '\u026F',
        'n': 'u',
        'o': 'o',
        'q': 'd',
        'p': 'b',
        's': 's',
        'u': 'π',
        'r': '\u0279',
        't': '\u0287',
        'v': '\u028C',
        'w': '\u028D',
        'y': '\u028E',
        'x': 'x',
        'z': 'z',
        '.': '\u02D9',
        '[': ']',
        '(': ')',
        '{': '}',
        '?': '\u00BF',
        '!': '\u00A1',
        "\'": ',',
        '<': '>',
        '_': '\u203E',
        '\u203F': '\u2040',
        '\u2045': '\u2046',
        '\u2234': '\u2235',
        '\r': '\n',
        'а': 'ɐ',
        'б': 'ƍ',
        'в': 'ʚ',
        'г': 'ɹ',
        'д': 'ɓ',
        'е': 'ǝ',
        'ё': 'ǝ',
        'ж': 'ж',
        'з': 'ε',
        'и': 'и',
        'й': 'ņ',
        'к': 'ʞ',
        'л': 'v',
        'м': 'w',
        'н': 'н',
        'о': 'о',
        'п': 'u',
        'р': 'd',
        'с': 'ɔ',
        'т': 'ɯ',
        'у': 'ʎ',
        'ф': 'ф',
        'х': 'х',
        'ц': 'ǹ',
        'ч': 'Һ',
        'ш': 'm',
        'щ': 'm',
        'ъ': 'q',
        'ы': 'ıq',
        'ь': 'q',
        'э': 'є',
        'ю': 'oı',
        'я': 'ʁ',
        ' ': ' ',
        '1': '\u0196',
        '2': '\u1105',
        '3': '\u0190',
        '4': '\u3123',
        '5': '\u03DB',
        '6': '9',
        '7': '\u3125',
        '8': '8',
        '9': '6',
        '0': '0'

    }

    @staticmethod
    def make(text: str) -> str:
        return ''.join([str(FlipTextMaker.flipTable.get(x, x)) for x in text.lower()])
