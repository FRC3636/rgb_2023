from patterns.pattern import Pattern, ChangeBehavior
from util.position import Position

class Just(Pattern):
    def __init__(self, inner, point = 0):
        super().__init__()
        self.inner = inner
        self.add_child(inner)
        self.point = point
        self.behavior = ChangeBehavior.STOP_FOLLOW

    def at(self, pos):
        return self.inner.at(Position(self.point, pos.total))

    def changeat(self, pos):
        self.inner.fullchangeat(Position(self.point, pos.total))
    
    def change(self):
        self.inner.fullchange()