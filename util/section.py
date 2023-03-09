from patterns.manipulate import Manipulated
from patterns.ranged import Ranged

def _flatten(l):
    if l == []:
        return l
    if isinstance(l[0], list):
        return _flatten(l[0]) + _flatten(l[1:])
    return l[:1] + _flatten(l[1:])

class LeafSection:
    def __init__(self, name, translation = 0, flipped = False):
        self.name = name
        self.translation = translation
        self.flipped = flipped
        self.preset = "none"
    
    def set_preset(self, preset):
        self.preset = preset

    def pattern(self, presets):
        f = lambda pos: pos.translate(self.translation)
        if self.flipped:
            f = lambda pos: pos.translate(self.translation).flip()
        return Manipulated(presets[self.preset], f)
    
    def get_children(self):
        return []

class ParentSection(LeafSection):
    def __init__(self, name, children):
        super().__init__(name)
        self.children = children
    
    def set_preset(self, preset):
        for s in self.children:
            s.set_preset(preset)
    
    def pattern(self, presets):
        return [s.pattern(presets) for s in self.children]
    
    def get_children(self):
        return self.children

class RootSection(ParentSection):
    def __init__(self, range, sections):
        super().__init__("root", sections)
        self.range = range
        self.all_sections = dict(map(lambda s: (s.name, s), _flatten([s.get_children() for s in self.children] + self.get_children())))
    
    def pattern(self, presets):
        return Ranged(self.range, _flatten([s.pattern(presets) for s in self.children]))
    
    def get_section(self, name):
        return self.all_sections[name]