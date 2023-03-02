from patterns.pattern import Pattern

class Memory(Pattern):
    def __init__(self, inner):
        super().__init__()
        self.add_child(inner)
        self.inner = inner
        self.values = {}
        self.positions = set()

    def at(self, pos):
        self.positions.add(pos)
        if pos in self.values.keys():
            return self.values[pos]
        val = self.inner.at(pos)
        self.values[pos] = val
        return val

    def change(self):
        for pos in self.positions:
            self.values[pos] = self.inner.at(pos)
    
    def changeat(self, pos):
        self.values[pos] = self.inner.at(pos)