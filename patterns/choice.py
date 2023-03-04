from patterns.pattern import Pattern
from random import choice

class Choice(Pattern):
    def __init__(self, *args, memory = True):
        super().__init__()
        self.children = args
        for child in args:
            self.add_child(child)
        self.actives = {}
        self.remembered = None
        self.memory = memory
    
    def at(self, pos):
        if self.memory:
            if self.remembered != pos.total:
                self.actives.clear()
                for i in range(pos.total):
                    self.actives[i] = choice(self.children)
                self.remembered = pos.total
            return self.actives[pos.ipos].at(pos)
        else:
            return choice(self.children).at(pos)
    
    def changeat(self, pos):
        self.actives[pos.ipos] = choice(self.children)