from patterns.pattern import Pattern, ChangeBehavior
from util.position import Position


class Ranged(Pattern):
    def __init__(self, maprange):
        super().__init__()
        for item in maprange.items:
            self.add_child(item[1][2])
        self.maprange = maprange
        self.behavior = ChangeBehavior.STOP_FOLLOW

    def at(self, pos):
        start, length, pattern = self.maprange.get(pos.ipos)
        return pattern.at(Position(pos.ipos - start, length))
    
    def changeat(self, pos):
        start, length, pattern = self.maprange.get(pos.ipos)
        return pattern.changeat(Position(pos.ipos - start, length))