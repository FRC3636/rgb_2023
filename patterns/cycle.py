from patterns.pattern import Pattern

class Cycle(Pattern):
    def __init__(self, *args):
        super().__init__()
        self.selected = 0
        self.children = args
        for child in args:
            self.add_child(child)
    
    def at(self, pos):
        return self.children[self.selected].at(pos)
    
    def change(self):
        self.selected = (self.selected + 1) % len(self.children)