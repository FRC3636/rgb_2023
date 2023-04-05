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
LEFT_ARM = lambda pattern: CombinedSection.ordered(
    pattern,
    PartSection(parts.LB_UP),
    PartSection(parts.LB_DOWN)
)
RIGHT_ARM = lambda pattern: CombinedSection.ordered(
    pattern,
    PartSection(parts.RB_UP),
    PartSection(parts.RB_DOWN)
)
ARMS = lambda pattern: CombinedSection.ordered(
    pattern,
    LEFT_ARM(pattern),
    RIGHT_ARM(pattern)
)
PANEL = lambda pattern: CombinedSection.ordered(pattern, PartSection(parts.PANEL))

ALL = lambda pattern: RootSection(CombinedSection.ordered(pattern, PartSection(parts.EVERYTHING)))