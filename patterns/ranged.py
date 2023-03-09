from patterns.pattern import Pattern
from util.position import Position

class Ranged(Pattern):
    def __init__(self, range, patterns):
        super().__init__()
        self.range = range
        self.patterns = patterns
        self._children = patterns

    def at(self, pos):
        selected = self.range.get(pos.ipos)
        return self.patterns[selected[0]].at(Position(pos.dpos - selected[1], selected[2] - selected[1]))