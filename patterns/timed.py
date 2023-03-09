from patterns.pattern import Pattern

class Timed(Pattern):
    def __init__(self, inner, frequency = 1):
        super().__init__()
        self.inner = inner
        self.add_child(inner)
        self.frequency = frequency
        self.time = 0

    def at(self, pos):
        return self.inner.at(pos)

    def update(self, dt, frame):
        self.time += dt
        while self.time >= 1 / self.frequency:
            self.time -= 1 / self.frequency
            self.inner.fullchange()