from patterns.pattern import Pattern


class Moving(Pattern):
    def __init__(self, inner, speed=1/3, floor=False):
        super().__init__()
        self.inner = inner
        self.add_child(inner)
        self.speed = speed
        self.floor = floor
        self.offset = 0

    def at(self, pos):
        p = pos.translate(self.offset * pos.total)
        if self.floor:
            p = p.floor()
        return self.inner.at(p)

    def update(self, dt, frame):
        self.offset = (self.offset + self.speed * dt) % 1
