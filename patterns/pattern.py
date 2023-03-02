from util import color
from enum import Enum

class Pattern:
    def __init__(self):
        self._children = []
        self.behavior = ChangeBehavior.PASS_FOLLOW

    def add_child(self, child):
        self._children.append(child)

    def at(self, pos):
        pass

    def update(self, dt):
        pass

    def fullupdate(self, dt):
        for child in self._children:
            child.fullupdate(dt)
        self.update(dt)

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

class ChangeBehavior(Enum):
    PASS_IGNORE = (True, False)
    PASS_FOLLOW = (True, True)
    STOP_IGNORE = (False, False)
    STOP_FOLLOW = (False, True)