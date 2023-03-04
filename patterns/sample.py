from patterns.pattern import Pattern
from util.position import Position
from random import randint

class Sample(Pattern):
    def __init__(self, inner):
        super().__init__()
        self.inner = inner
        self.add_child(inner)

    def at(self, pos):
        return self.inner.at(Position(randint(0, pos.total), pos.total))