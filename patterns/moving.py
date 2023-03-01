from patterns.pattern import Pattern

class Moving(Pattern):
    def __init__(self, inner, speed = 1/3):
        super().__init__()
        self.inner = inner
        self.add_child(inner)
        self.speed = speed
        self.offset = 0

    def at(self, pos):
        return self.inner.at((pos + self.offset) % 1)

    def update(self, dt):
        self.offset = (self.offset + self.speed * dt) % 1