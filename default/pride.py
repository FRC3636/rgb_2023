from random import choice

from util.preset import Preset
from util import color

from default import sections, patterns

from patterns.solid import Solid

_pride_flag = lambda name, *colors: Preset("panel", f"pride_{name}", lambda _: sections.PANEL_INDICATOR(
    patterns.pride_flag(*colors), Solid(colors[0]), Solid(colors[-1])
))

_transpink = color.Color(0xF5, 0xA9, 0xB8)
_transblue = color.Color(0x5B, 0xCE, 0xFA)
TRANSRIGHTS = _pride_flag("trans", _transblue, _transpink, color.white, _transpink, _transblue)

_enbyyellow = color.Color(0xFC, 0xF4, 0x34)
_enbypurple = color.Color(0x9C, 0x59, 0xD1)
ENBY = _pride_flag("enby", _enbyyellow, color.white, _enbypurple, color.black)

_bipink = color.Color(0xD6, 0x02, 0x70)
_bipurple = color.Color(0x9B, 0x4F, 0x96)
_biblue = color.Color(0x00, 0x38, 0xA8)
BI = _pride_flag("bi", _bipink, _bipurple, _biblue)

_panpink = color.Color(0xFF, 0x21, 0x8C)
_panyellow = color.Color(0xFF, 0xD8, 0x00)
_pancyan = color.Color(0x21, 0xB1, 0xFF)
PAN = _pride_flag("pan", _panpink, _panyellow, _pancyan)

_genderfluidpink = color.Color(0xFF, 0x76, 0xA4)
_genderfluidpurple = color.Color(0xC0, 0x11, 0xD7)
_genderfluidblue = color.Color(0x2F, 0x3C, 0xBE)
GENDERFLUID = _pride_flag("genderfluid", _genderfluidpink, color.white, _genderfluidpurple, color.black, _genderfluidblue)

_acegray = color.Color(0xA3, 0xA3, 0xA3)
_acepurple = color.Color(0x80, 0x00, 0x80)
ACE = _pride_flag("ace", color.black, _acegray, color.white, _acepurple)

_arogreen = color.Color(0x3D, 0xA5, 0x42)
_arolgreen = color.Color(0xA7, 0xD3, 0x79)
_arogray = color.Color(0xA9, 0xA9, 0xA9)
ARO = _pride_flag("aro", _arogreen, _arolgreen, color.white, _arogray, color.black)

_aroaceorange = color.Color(0xEF, 0x90, 0x07)
_aroaceyellow = color.Color(0xF6, 0xD3, 0x17)
_aroaceskyblue = color.Color(0x45, 0xBC, 0xEE)
_aroacenavy = color.Color(0x1E, 0x3F, 0x54)
AROACE = _pride_flag("aroace", _aroaceorange, _aroaceyellow, color.white, _aroaceskyblue, _aroacenavy)

_lesbianred = color.Color(0xD6, 0x29, 0x00)
_lesbianorange = color.Color(0xFF, 0x9B, 0x55)
_lesbianpink = color.Color(0xD4, 0x61, 0xA6)
_lesbianpurple = color.Color(0xA5, 0x00, 0x62)
LESBIAN = _pride_flag("lesbian", _lesbianred, _lesbianorange, color.white, _lesbianpink, _lesbianpurple)

_mlmgreen = color.Color(0x07, 0x8D, 0x70)
_mlmlgreen = color.Color(0x98, 0xE8, 0xC1)
_mlmlblue = color.Color(0x7B, 0xAD, 0xE2)
_mlmpurple = color.Color(0x3D, 0x1A, 0x78)
MLM = _pride_flag("mlm", _mlmgreen, _mlmlgreen, color.white, _mlmlblue, _mlmpurple)

_rainbowred = color.Color(0xE4, 0x03, 0x03)
_rainboworange = color.Color(0xFF, 0x8C, 0x00)
_rainbowyellow = color.Color(0xFF, 0xED, 0x00)
_rainbowgreen = color.Color(0x00, 0x80, 0x26)
_rainbowblue = color.Color(0x24, 0x40, 0x8E)
_rainbowpurple = color.Color(0x73, 0x29, 0x82)
RAINBOW = _pride_flag("rainbow", _rainbowred, _rainboworange, _rainbowyellow, _rainbowgreen, _rainbowblue, _rainbowpurple)

_agenderisyou = color.Color(0xBA, 0xBA, 0xBA)
_agendergreen = color.Color(0xBA, 0xF5, 0x84)
AGENDER = _pride_flag("agender", color.black, _agenderisyou, color.white, _agendergreen)

_bigenderpink = color.Color(0xC4, 0x79, 0xA2)
_bigenderlpink = color.Color(0xED, 0xA5, 0xCD)
_bigenderlavender = color.Color(0xD6, 0xC7, 0xE8)
_bigenderlblue = color.Color(0x9A, 0xC7, 0xE8)
_bigenderblue = color.Color(0x6D, 0x82, 0xD1)
BIGENDER = _pride_flag("bigender", _bigenderpink, _bigenderlpink, _bigenderlavender, color.white, _bigenderlavender, _bigenderlblue, _bigenderblue)

RANDOM_PRIDE_FLAG = choice([
    TRANSRIGHTS, ENBY, BI, PAN, GENDERFLUID, ACE, ARO, AROACE, LESBIAN, MLM, RAINBOW, AGENDER, BIGENDER
])