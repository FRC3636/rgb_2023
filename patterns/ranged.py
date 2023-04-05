from patterns.pattern import Pattern, ChangeBehavior
from util.position import Position
from util.color import black


class Ranged(Pattern):
    def __init__(self, maprange):
        super().__init__()
        for item in maprange.items:
            self.add_child(item[1].pattern)
        self.maprange = maprange
        self.behavior = ChangeBehavior.STOP_FOLLOW

    def at(self, pos):
        val = self.maprange.get(pos.ipos)
        if val != None:
            return val.pattern.at(Position(pos.ipos - val.start, val.length))
        else:
            return black
    
    def changeat(self, pos):
        val = self.maprange.get(pos.ipos)
        if val != None:
            return val.pattern.changeat(Position(pos.ipos - val.start, val.length))