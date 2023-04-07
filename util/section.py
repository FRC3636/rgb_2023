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
        raise RuntimeError(f"unimplemented on {self}")

    def length(self):
        raise RuntimeError(f"unimplemented on {self}")


class MultiSection(Section):
    def __init__(self, *children, **kwargs):
        super().__init__(**kwargs)
        self.children = children
    
    def __repr__(self):
        return f"{self.__class__.__name__} {self.children}"


class RootSection(MultiSection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ranges = []
        for section in self.children:
            ranges += section.compute_range()
        range = MappedRange(
            *map(lambda x: (x.part.range, x.patternize()), ranges))
        self.pat = Ranged(range)

    def pattern(self):
        return self.pat


class SectionSpec:
    def __init__(self, section, start):
        self.section = section
        self.start = start


class CombinedSection(MultiSection):
    def __init__(self, pattern, length, *sections, **kwargs):
        self.sections = sections
        super().__init__(*map(lambda x: x.section, sections), **kwargs)
        self.pattern = pattern
        self.len = length

    def compute_range(self):
        ranges = []
        for spec in self.sections:
            r = spec.section.compute_range()
            ranges += map(lambda x: x.with_pattern(self.pattern,
                          self.len).transform_by(self.transform).add(spec.start), r)
        return ranges

    def length(self):
        return self.len

    @classmethod
    def ordered(cl, pattern, *children, **kwargs):
        length = 0
        positioned_children = []
        for child in children:
            positioned_children.append(SectionSpec(child, length))
            length += child.length()
        return CombinedSection(pattern, length, *positioned_children, **kwargs)


class DistinctSection(MultiSection):
    def __init__(self, patterns, *args, **kwargs):
        self.patterns = patterns
        super().__init__(*args, **kwargs)

    def compute_range(self):
        ranges = []
        for i, section in enumerate(self.children):
            r = section.compute_range()
            ranges += map(lambda x: x.with_pattern(
                self.patterns[i], x.length), r)
        return ranges

    @classmethod
    def all(self, pattern, *children, **kwargs):
        return DistinctSection([pattern] * len(children), *children, **kwargs)


class PartSection(Section):
    def __init__(self, part, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.part = part

    def compute_range(self):
        return [_SectionData(self.part).transform_by(self.transform)]

    def length(self):
        return self.part.length()
    
    def __repr__(self):
        return f"{self.__class__.__name__} ({self.part})"


class _PatternData:
    def __init__(self, start, pattern, offset, length):
        self.pattern = pattern
        self.start = start
        self.offset = offset
        self.length = length


class _SectionData:
    def __init__(self, part, transform=SectionTransform()):
        self.part = part
        self.transform = transform
        self.pattern = None
        self.length = part.length()
        self.offset = 0

    def with_pattern(self, pattern, length):
        self.pattern = pattern
        self.length = length
        return self

    def transform_by(self, transform):
        self.transform = self.transform.plus(transform)
        return self

    def add(self, val):
        self.offset += val
        return self

    def patternize(self):
        return _PatternData(self.part.start, self.transform.apply(self.pattern), self.offset, self.length)
