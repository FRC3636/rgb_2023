from util.color import blend
from colour import Color
from patterns.pattern import Pattern
from patterns.solid import SolidPattern

class BreathePattern(Pattern):
    def __init__(self, on, off = SolidPattern(Color("black")), speed = 2):
        self.on = on
        self.off = off
        self.speed = speed
        self.state = 0
    
    def at(self, pos):
        progress = self.state
        if progress > 1:
            progress = 2 - progress
        return blend(
            self.on.at(pos),
            self.off.at(pos),
            progress
        )

    def update(self, dt):
        self.state = (self.state + (self.speed * 2) * dt) % 2