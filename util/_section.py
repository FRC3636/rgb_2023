from patterns.manipulate import Manipulated
from patterns.ranged import Ranged
from util.range import MappedRange

def _flatten(l):
    if l == []:
        return l
    if isinstance(l[0], list):
        return _flatten(l[0]) + _flatten(l[1:])
    return l[:1] + _flatten(l[1:])


class SectionTransform:
    def __init__(self, translate=0, reverse=False):
        self.translate = translate
        self.reverse = reverse

    def plus(self, other):
        return SectionTransform(self.translate + other.translate, self.reverse ^ other.reverse)

    def apply(self, pattern):
        if self.reverse:
            return Manipulated(pattern, lambda pos: pos.translate(self.translate).flip())
        else:
            return Manipulated(pattern, lambda pos: pos.translate(self.translate))


class Section:
    def __init__(self, transform=SectionTransform()):
        self.transform = transform
    
    def compute_range(self):
        raise "unimplemented"


class MultiSection(Section):
    def __init__(self, *children, **kwargs):
        super().__init__(**kwargs)
        self.children = children
        
        
class SectionSpec:
    def __init__(self, section, start, length):
        self.section = section
        self.start = start
        self.length = length


class CombinedSection(MultiSection):
    def __init__(self, pattern, length, *sections, **kwargs):
        self.sections = sections
        super().__init__(*map(lambda x: x.section, sections), **kwargs)
        self.pattern = pattern
        self.length = length
    
    def compute_range(self):
        ranges = []
        start = 0
        for section in self.sections:
            ranges.append(((part.start, part.end), (start, l, part.transform.apply(section.pattern))))
            start += length
        ranges.sort(key=lambda x: x[0][0])
        r = MappedRange(*ranges)
        return Ranged(r)

    @classmethod
    def ordered(pattern, *children, **kwargs):
        length = 0
        positioned_children = []
        for child in children:
            positioned_children.append(SectionSpec(length, child))
            length += child.length
        return CombinedSection(pattern, length, *positioned_children, **kwargs)


class PartSection(Section):
    def __init__(self, part, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.part = part
    
    def compute_range(self):
        return [ _SectionData(self).transform_by(self.transform) ]


class _SectionData:
    def __init__(self, part, transform=SectionTransform()):
        self.part = part
        self.transform = transform
        self.pattern = None
        self.pos = 0
    
    def with_pattern(self, pattern):
        self.pattern = pattern
        return self
    
    def transform_by(self, transform):
        self.transform = self.transform.plus(transform)
        return self
        
    def add(self, val):
        self.pos += val
        return self
    
    def pattern(self):
        return self.transform.apply(self.pattern)