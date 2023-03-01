from patterns.pattern import Pattern
from util import color

import math

class Gradient(Pattern):
    def __init__(self, *colors):
        super().__init__()
        self.colors = colors
    
    def at(self, pos):
        f = pos * (len(self.colors) - 1)
        oneLower = int(math.floor(f))
        oneHigher = int(math.ceil(f))

        start = oneLower / (len(self.colors) - 1)
        end = oneHigher / (len(self.colors) - 1)
        diff = end - start

        if oneLower != oneHigher:
            position = (pos - start) / diff
        else:
            position = 0

        color1 = self.colors[oneLower]
        color2 = self.colors[oneHigher]
        return color.blend(color1, color2, position)