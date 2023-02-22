import math
from patterns.pattern import Pattern

class HybridPattern(Pattern):
    def __init__(self, *args):
        self.children = args
    
    def at(self, pos):
        length = len(self.children)
        selected = math.floor(min(pos * length, length - 1))
        return self.children[selected].at(pos - (1 / (length - selected + 1)))