from util import color

class Pattern:
    def __init__(self):
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def at(self, pos):
        pass

    def update(self, dt):
        pass

    def change(self):
        pass

    def fullupdate(self, dt):
        for child in self._children:
            child.fullupdate(dt)
        self.update(dt)