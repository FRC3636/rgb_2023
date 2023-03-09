from patterns.pattern import Pattern, ChangeBehavior

class Manipulated(Pattern):
    def __init__(self, inner, func):
        super().__init__()
        self.inner = inner
        self.add_child(inner)
        self.func = func
        self.behavior = ChangeBehavior.STOP_FOLLOW
    
    def at(self, pos):
        return self.inner.at(self.func(pos))
    
    def changeat(self, pos):
        return self.inner.fullchangeat(self.func(pos))
    
    def change(self):
        self.inner.fullchange()