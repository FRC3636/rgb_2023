from default.parts import *

from util.section import *

BODY = CombinedSection(
    PartSection(BODY1),
    PartSection(BODY2),
    PartSection(BODY3),
    PartSection(BODY4),
    PartSection(BODY5),
    PartSection(BODY6),
    PartSection(BODY7),
    PartSection(BODY8),
    PartSection(BODY9)
)
LEFT_ARM = CombinedSection(
    PartSection(LB_UP),
    PartSection(LB_DOWN)
)
RIGHT_ARM = CombinedSection(
    PartSection(RB_UP),
    PartSection(RB_DOWN)
)
PANEL = PartSection(PANEL)