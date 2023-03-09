from patterns.pattern import SizedPattern
from patterns.solid import Solid
from util.position import Position
from util import color
from random import choice

class Rain(SizedPattern):
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
    
    def new_size(self, size):
        self.brightnesses.clear()
        for i in range(size):
            self.brightnesses[i] = 0

    def at(self, pos):
        super().at(pos)
        self.brightnesses[pos.ipos] = self.brightnesses.get(pos.ipos) or 0
        return color.blend(
            self.off.at(pos),
            self.inner.at(pos),
            self.brightnesses[pos.ipos]
        )

    def update(self, dt, frame):
        self.time += dt * self.speed
        while self.time >= 1:
            self.time -= 1
            self.brightnesses[choice(list(self.brightnesses.keys()))] = 1
        if self.remembered != None:
            for i in range(self.remembered):
                val = max(0, self.brightnesses[i] - self.decay * dt)
                self.brightnesses[i] = val
                if val == 0:
                    self.inner.fullchangeat(Position(i, self.remembered))