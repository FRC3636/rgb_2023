from patterns.pattern import Pattern
from patterns.solid import Solid
from util import color
from random import choice

class Rain(Pattern):
    def __init__(self, inner, off = Solid(color.black), speed = 30, decay = 1):
        super().__init__()
        self.add_child(inner)
        self.add_child(off)
        self.inner = inner
        self.off = off
        self.brightnesses = {}
        self.time = 0
        self.speed = speed
        self.decay = decay
    
    def at(self, pos):
        self.brightnesses[pos] = self.brightnesses.get(pos) or 0
        return color.blend(self.off.at(pos), self.inner.at(pos), self.brightnesses[pos])

    def update(self, dt):
        self.time += dt * self.speed
        remainder = self.time % 1
        total = int(self.time - remainder)
        for i in range(total):
            self.brightnesses[choice(list(self.brightnesses.keys()))] = 1
        self.time = remainder
        for i in self.brightnesses.keys():
            val = max(0, self.brightnesses[i] - self.decay * dt)
            self.brightnesses[i] = val
            if val == 0:
                self.inner.fullchangeat(i)