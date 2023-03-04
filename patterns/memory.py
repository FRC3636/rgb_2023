from patterns.pattern import SizedPattern
from util.position import Position

class Memory(SizedPattern):
    def __init__(self, inner):
        super().__init__()
        self.add_child(inner)
        self.inner = inner
        self.values = {}

    def new_size(self, size):
        self.values.clear()
        for i in range(size):
            self.values[i] = self.inner.at(Position(i, size))

    def at(self, pos):
        super().at(pos)
        return self.values[pos.ipos]

    def change(self):
        self.values.clear()
        self.remembered = None
    
    def changeat(self, pos):
        self.values[pos.ipos] = self.inner.at(pos)