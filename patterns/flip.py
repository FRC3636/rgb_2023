from patterns.pattern import Pattern

class Flip(Pattern):
    def __init__(self, inner):
        super().__init__()
        self.inner = inner
        self.add_child(inner)

    def at(self, pos):
        return self.inner.at(pos.flip())