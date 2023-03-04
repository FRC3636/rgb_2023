import math
from patterns.pattern import Pattern
from util.position import Position

class Hybrid(Pattern): # FIXME: doesn't handle changes properly?
    def __init__(self, *args):
        super().__init__()
        for child in args:
            self.add_child(child)
        self.children = args
    
    def at(self, pos):
        length = len(self.children)
        selected = math.floor(min(pos.pos * length, length - 1))
        return self.children[selected].at(
            pos
                .translate(-1 / length * selected)
                .scale(1 / length)
        )
    
    def changeat(self, pos):
        length = len(self.children)
        selected = math.floor(min(pos.pos * length, length - 1))
        self.children[selected].fullchangeat(
            pos
                .translate(-1 / length * selected)
                .scale(1 / length)
        )