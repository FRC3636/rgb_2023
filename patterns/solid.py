from patterns.pattern import Pattern

class Solid(Pattern):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def at(self, pos):
        return self.color