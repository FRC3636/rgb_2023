from patterns.pattern import SizedPattern
from util.position import Position
from util import color

class Smooth(SizedPattern):
    def __init__(self, inner, time = 1):
        super().__init__()
        self.inner = inner
        self.add_child(inner)
        self.time = time

        self.sources = {}
        self.currents = {}
        self.progresses = {}

    def new_size(self, size):
        self.sources.clear()
        self.currents.clear()
        self.progresses.clear()
        for i in range(size):
            color = self.inner.at(Position(i, size))
            self.sources[i] = color
            self.currents[i] = color
            self.progresses[i] = 0

    def at(self, pos):
        super().at(pos)
        return self.currents[pos.ipos]

    def update(self, dt, frame):
        change = dt / self.time
        if self.remembered != None:
            for i in range(self.remembered):
                self.progresses[i] = min(1, self.progresses[i] + change)
                self.currents[i] = color.blend(
                    self.sources[i],
                    self.inner.at(Position(i, self.remembered)),
                    self.progresses[i]
                )

    def changeat(self, pos):
        self.sources[pos.ipos] = self.currents[pos.ipos]
        self.progresses[pos.ipos] = 0

    def change(self):
        if self.remembered != None:
            for i in range(self.remembered):
                self.sources[i] = self.currents[i]
                self.progresses[i] = 0