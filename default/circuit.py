from util.part import Part
from util.section import PartSection, SectionTransform, RootSection, CombinedSection, SectionSpec

#FIXME: not quite right

# --- parts ---
CBODY1 = Part("body1", 0, 12)
CBODY2 = Part("body2", 12, 24)
CBODY3 = Part("body3", 75, 82)
CBODY4_LEFT = Part("cbody4_left", 82, 87)
CBODY4_LCENTER = Part("cbody4_lcenter", 87, 100) # 13 long
CBODY4_RCENTER = Part("cbody4_rcenter", 100, 112) # 12 long
CBODY4_RIGHT = Part("cbody4_right", 112, 117)
CBODY5 = Part("body5", 117, 129)
CBODY6 = Part("body6", 181, 188)
CBODY7 = Part("body7", 188, 202)
CBODY8 = Part("body8", 202, 209)
CBODY9 = Part("body9", 280, 287)

# --- part sections ---
SBODY1 = PartSection(CBODY1, SectionTransform(reverse=True))
SBODY2 = PartSection(CBODY2)
SBODY3 = PartSection(CBODY3, SectionTransform(reverse=True))
SBODY4_LEFT = PartSection(CBODY4_LEFT, SectionTransform(reverse=True))
SBODY4_LCENTER = PartSection(CBODY4_LCENTER, SectionTransform(reverse=True))
SBODY4_RCENTER = PartSection(CBODY4_RCENTER)
SBODY4_RIGHT = PartSection(CBODY4_RIGHT)
SBODY5 = PartSection(CBODY5)
SBODY6 = PartSection(CBODY6, SectionTransform(reverse=True))
SBODY7 = PartSection(CBODY7)
SBODY8 = PartSection(CBODY8)
SBODY9 = PartSection(CBODY9, SectionTransform(reverse=True))

# --- sections ---
_lcenter_start = 0
_rcenter_start = -3
_left_start = SBODY4_LCENTER.length()
_right_start = SBODY4_RCENTER.length() + _rcenter_start
_leftmiddle_start = SBODY4_LCENTER.length() + _lcenter_start
_rightmiddle_start = SBODY4_RCENTER.length() + _rcenter_start
_leftside_start = _left_start + SBODY4_LEFT.length()
_leftside2_start = _leftside_start + SBODY1.length()
_rightside_start = _right_start + SBODY4_RIGHT.length()
_rightside2_start = _rightside_start + SBODY7.length()
CIRCUIT = lambda pattern: CombinedSection(
    pattern,
    _rightside2_start + SBODY8.length(),
    SectionSpec(SBODY4_LCENTER, _lcenter_start),
    SectionSpec(SBODY4_RCENTER, _rcenter_start),
    SectionSpec(SBODY3, _leftmiddle_start),
    SectionSpec(SBODY6, _rightmiddle_start),
    SectionSpec(SBODY4_LEFT, _left_start),
    SectionSpec(SBODY4_RIGHT, _right_start),
    SectionSpec(SBODY1, _leftside_start),
    SectionSpec(SBODY2, _leftside_start),
    SectionSpec(SBODY5, _rightside_start),
    SectionSpec(SBODY7, _rightside_start),
    SectionSpec(SBODY8, _rightside2_start),
    SectionSpec(SBODY9, _leftside2_start)
)