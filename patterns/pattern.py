from enum import Enum

class Pattern:
    def __init__(self):
        self._children = []
        self.behavior = ChangeBehavior.PASS_FOLLOW
        self.last_frame = -1

    def add_child(self, child):
        self._children.append(child)

    def at(self, pos):
        pass

    def update(self, dt, frame):
        pass

    def fullupdate(self, dt, frame):
        if frame == self.last_frame:
            return
        self.last_frame = frame
        for child in self._children:
            child.fullupdate(dt, frame)
        self.update(dt, frame)

    def change(self):
        pass

    def fullchange(self):
        behavior = self.behavior.value
        if behavior[0]:
            for child in self._children:
                child.fullchange()
        if behavior[1]:
            self.change()
    
    def changeat(self, pos):
        pass

    def fullchangeat(self, pos):
        behavior = self.behavior.value
        if behavior[0]:
            for child in self._children:
                child.fullchangeat(pos)
        if behavior[1]:
            self.changeat(pos)
    
    def behavior(self, behavior):
        self.behavior = behavior
        return self

class SizedPattern(Pattern):
    def __init__(self):
        super().__init__()
        self.remembered = None

    def new_size(self, size):
        pass

    def at(self, pos):
        if pos.total != self.remembered:
            self.remembered = pos.total
            self.new_size(pos.total)

class ChangeBehavior(Enum):
    PASS_IGNORE = (True, False)
    PASS_FOLLOW = (True, True)
    STOP_IGNORE = (False, False)
    STOP_FOLLOW = (False, True)