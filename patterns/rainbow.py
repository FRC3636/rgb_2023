from util import color
from patterns.pattern import Pattern

class Rainbow(Pattern):
    def __init__(self, saturation = 1, value = 0.5):
        super().__init__()
        self.saturation = saturation
        self.value = value
        self.offset = 0
    
    def at(self, pos):
        return color.hsv(pos, self.saturation, self.value)
    
    def update(self, dt):
        self.offset += dt