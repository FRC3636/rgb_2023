from patterns.manipulate import Manipulated
from patterns.ranged import Ranged
from util.range import MappedRange

def _flatten(l):
    if l == []:
        return l
    if isinstance(l[0], list):
        return _flatten(l[0]) + _flatten(l[1:])
    return l[:1] + _flatten(l[1:])


class Layout:
    def __init__(self, *sections):
        self.sections = sections

    def pattern(self):
        ranges = []
        for section in self.sections:
            l = 0
            for part in section.parts:
                l += part.length()
            start = 0
            for part in section.parts:
                length = part.length()
                ranges.append(((part.start, part.end), (start, l, part.transform.apply(section.pattern))))
                start += length
        ranges.sort(key=lambda x: x[0][0])
        r = MappedRange(*ranges)
        return Ranged(r)


class Section:
    def __init__(self, pattern, *parts):
        self.pattern = pattern
        self.parts = parts


class PartTransform:
    def __init__(self, translate=0, reverse=False):
        self.translate = translate
        self.reverse = reverse

    def apply(self, pattern):
        if self.reverse:
            return Manipulated(pattern, lambda pos: pos.translate(self.translate).flip())
        else:
            return Manipulated(pattern, lambda pos: pos.translate(self.translate))


class Part:
    # exclusive of upper bound
    def __init__(self, range, transform=PartTransform()):
        self.start, self.end = range
        self.transform = transform

    def length(self):
        return self.end - self.start
