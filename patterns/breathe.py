import math

from util import color
from patterns.pattern import Pattern
from patterns.solid import Solid

class Breathe(Pattern):
    def __init__(self, on, off = Solid(color.black), speed = 4):
        super().__init__()
        self.on = on
        self.off = off
        self.speed = speed
        self.time = 0
        self.current = 0.5
        self.direction = 1

    def at(self, pos):
        return color.blend(
            self.on.at(pos),
            self.off.at(pos),
            self.current
        )

    def update(self, dt, frame):
        self.time = self.time + dt * self.speed % (math.pi * 2)
        new = (math.sin(self.time) + 1) / 2
        if new >= self.current and self.direction == -1:
            self.off.fullchange()
            self.direction = 1
        elif new <= self.current and self.direction == 1:
            self.on.fullchange()
            self.direction = -1
        self.current = new