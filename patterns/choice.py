from patterns.pattern import Pattern
from random import choice

class Choice(Pattern):
    def __init__(self, *args):
        super().__init__()
        self.children = args
        for child in args:
            self.add_child(child)
    
    def at(self, pos):
        return choice(self.children).at(pos)