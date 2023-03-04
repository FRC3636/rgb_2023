from patterns.pattern import Pattern
from util.position import Position
import math

class Scaled(Pattern):
    def __init__(self, inner, scale, wrapping = True):
        super().__init__()
        self.inner = inner
        self.add_child(inner)
        self.scale = scale
        self.wrapping = wrapping

    def at(self, pos):
        newpos = math.ceil(pos.dpos / self.scale)
        if self.wrapping:
            newpos %= pos.total
        return self.inner.at(
            Position(newpos, pos.total)
        )