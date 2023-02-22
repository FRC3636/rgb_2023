from patterns.pattern import Pattern

class ScaledPattern(Pattern):
    def __init__(self, inner, scale):
        self.inner = inner
        self.scale = scale

    def at(self, pos):
        return self.inner.at((pos / self.scale) % 1)