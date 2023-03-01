from patterns.pattern import Pattern

class Scaled(Pattern):
    def __init__(self, inner, scale, wrapping = True):
        super().__init__()
        self.inner = inner
        self.add_child(inner)
        self.scale = scale
        self.wrapping = wrapping

    def at(self, pos):
        p = (pos / self.scale)
        if self.wrapping:
            p %= 1
        return self.inner.at(p)