from patterns.pattern import Pattern
from util import color
from random import random

def _get_randomized(v):
    if v == None:
        return random()
    return v

class Noise(Pattern):
    def __init__(self, hue = None, saturation = None, value = None):
        super().__init__()
        self.hue = hue
        self.saturation = saturation
        self.value = value
    
    def at(self, pos):
        return color.hsv(_get_randomized(self.hue), _get_randomized(self.saturation), _get_randomized(self.value))