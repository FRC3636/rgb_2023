from patterns.pattern import Pattern

class Just(Pattern):
    def __init__(self, inner, point = 0):
        super().__init__()
        self.inner = inner
        self.add_child(inner)
        self.point = point

    def at(self, pos):
        return self.inner.at(self.point)