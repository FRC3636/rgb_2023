from default import parts

from util.section import *

BODY = lambda pattern: CombinedSection.ordered(
    pattern,
    PartSection(parts.BODY1),
    PartSection(parts.BODY2),
    PartSection(parts.BODY3),
    PartSection(parts.BODY4),
    PartSection(parts.BODY5),
    PartSection(parts.BODY6),
    PartSection(parts.BODY7),
    PartSection(parts.BODY8),
    PartSection(parts.BODY9)
)
LB_UP = PartSection(parts.LB_UP)
LB_DOWN = PartSection(parts.LB_DOWN, SectionTransform(reverse=True))
LEFT_ARM = lambda pattern: CombinedSection.ordered(
    pattern,
    LB_UP,
    LB_DOWN
)
RB_UP = PartSection(parts.RB_UP)
RB_DOWN = PartSection(parts.RB_DOWN, SectionTransform(reverse=True, translate=6))
RIGHT_ARM = lambda pattern: CombinedSection.ordered(
    pattern,
    RB_UP,
    RB_DOWN
)
ARMS = lambda pattern: CombinedSection.ordered(
    pattern,
    LEFT_ARM(pattern),
    RIGHT_ARM(pattern)
)
SYM_ARMS = lambda pattern: DistinctSection.all(
    pattern,
    LB_UP,
    LB_DOWN,
    RB_UP,
    RB_DOWN
)
PANEL = lambda pattern: DistinctSection.all(pattern, PartSection(parts.PANEL))

ALL = lambda pattern: RootSection(DistinctSection.all(pattern, PartSection(parts.EVERYTHING)))