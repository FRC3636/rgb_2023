from patterns.pattern import Pattern

class SolidPattern(Pattern):
    def __init__(self, color):
        self.color = color

    def at(self, pos):
        return self.color