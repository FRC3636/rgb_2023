from patterns.pattern import Pattern
from patterns.manipulate import Manipulated
from util.position import Position

class Scaled(Pattern):
    def __init__(self, inner, scale, wrapping = True):
        super().__init__()
        self.inner = inner
        self.add_child(inner)
        self.scale = scale
        self.wrapping = wrapping

    def at(self, pos):
        newpos = pos.dpos / self.scale
        return self.inner.at(
            Position(newpos, pos.total)
        )

ScaledTo = lambda inner, scale: Manipulated(inner, lambda pos: Position(pos.dpos, scale))