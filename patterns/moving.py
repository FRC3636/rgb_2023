from patterns.pattern import Pattern

class MovingPattern(Pattern):
    def __init__(self, inner, speed = 1/3):
        self.inner = inner
        self.speed = speed
        self.offset = 0

    def at(self, pos):
        return self.inner.at((pos + self.offset) % 1)

    def update(self, dt):
        self.offset = (self.offset + self.speed * dt) % 1