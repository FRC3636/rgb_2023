from util import color
from patterns.pattern import Pattern
from functools import cache

class Rainbow(Pattern):
    def __init__(self, chroma = 50, lightness = 65):
        super().__init__()
        self.chroma = chroma
        self.lightness = lightness
    
    def at(self, pos):
        return self._at(round(pos.pos, 2))

    @cache
    def _at(self, cpos):
        return color.lch(self.lightness, self.chroma, cpos * 360)