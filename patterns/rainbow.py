from colour import Color
from patterns.pattern import Pattern

class RainbowPattern(Pattern):
    def __init__(self, saturation = 1, lightness = 0.5):
        self.saturation = saturation
        self.lightness = lightness
        self.offset = 0
    
    def at(self, pos):
        return Color(hsl = (pos, self.saturation, self.lightness))
    
    def update(self, dt):
        self.offset += dt