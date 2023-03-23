from patterns.pattern import SizedPattern
from util import color

_morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    ' ': ' '
}

for key, val in _morse.items():
    modified = val.replace(" ", "  ").replace("-", "### ").replace(".", "# ")
    _morse[key] = map(lambda x: x == "#", modified.split(""))

class Morse(SizedPattern):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg
        self.states = []
        for i, char in enumerate(self.msg):
            self.states[i] += _morse[char]

    def at(self, pos):
        super().at(pos)
        if len(self.states) <= pos.ipos:
            return color.black
        else:
            if self.states[pos.ipos]:
                return color.white
            else:
                return color.black