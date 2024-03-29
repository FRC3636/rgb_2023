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
RB_DOWN = PartSection(parts.RB_DOWN, SectionTransform(translate=6))
RIGHT_ARM = lambda pattern: CombinedSection.ordered(
    pattern,
    RB_UP,
    RB_DOWN
)
UPS = lambda pattern: DistinctSection.all(pattern, RB_UP, LB_UP)
DOWNS = lambda pattern: DistinctSection.all(pattern, RB_DOWN, LB_DOWN)
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
PANEL = lambda pattern: CombinedSection.ordered(
    pattern,
    PartSection(parts.PANEL_BOTTOM),
    PartSection(parts.PANEL_RIGHT),
    PartSection(parts.PANEL_TOP),
    PartSection(parts.PANEL_LEFT)
)
PANEL_INDICATOR = lambda sides, top, bottom: DistinctSection(
    [ bottom, sides, top, sides ],
    PartSection(parts.PANEL_BOTTOM),
    PartSection(parts.PANEL_RIGHT),
    PartSection(parts.PANEL_TOP),
    PartSection(parts.PANEL_LEFT, SectionTransform(reverse=True))
)

ALL = lambda pattern: RootSection(DistinctSection.all(pattern, PartSection(parts.EVERYTHING)))