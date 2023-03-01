import math
from patterns.pattern import Pattern

class Hybrid(Pattern):
    def __init__(self, *args):
        super().__init__()
        for child in args:
            self.add_child(child)
        self.children = args
    
    def at(self, pos):
        length = len(self.children)
        selected = math.floor(min(pos * length, length - 1))
        return self.children[selected].at(pos - (1 / (length - selected + 1)))