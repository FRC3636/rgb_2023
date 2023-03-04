from patterns.pattern import Pattern
from util.position import Position
import math

class Moving(Pattern):
    def __init__(self, inner, speed = 1/3):
        super().__init__()
        self.inner = inner
        self.add_child(inner)
        self.speed = speed
        self.offset = 0

    def at(self, pos):
        return self.inner.at(pos.translate(self.offset * pos.total))

    def update(self, dt):
        self.offset = (self.offset + self.speed * dt) % 1