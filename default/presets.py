from util.preset import Preset
from util import section

from default import sections, patterns, circuit

DEFAULT = Preset("root", "default", lambda children: section.RootSection(*children), [ "body", "arms", "panel" ])
ESTOP = Preset("root", "estop", lambda _: sections.ALL(patterns.solid_red))
DISCONNECTED = Preset("root", "disconnected", lambda _: sections.ALL(patterns.solid_blue))
BALANCED = Preset("root", "balanced", lambda children: sections.RootSection(
    *children, sections.SYM_ARMS(patterns.rainbow), sections.PANEL(patterns.rainbow)
), [ "body" ])

_wrainbow = lambda name, func: Preset(name, f"wrainbow_{name}", lambda _: func(patterns.whole_rainbow))
WRAINBOW_ARMS = _wrainbow("arms", sections.ARMS)
WRAINBOW_BODY = _wrainbow("body", sections.BODY)
WRAINBOW_PANEL = _wrainbow("panel", sections.PANEL)

_rainbow = lambda name, func: Preset(name, f"rainbow_{name}", lambda _: func(patterns.slow_rainbow))
RAINBOW_ARMS = _rainbow("arms", sections.SYM_ARMS)
RAINBOW_BODY = _rainbow("body", sections.BODY)
RAINBOW_PANEL = _rainbow("body", sections.PANEL)

CUBE = Preset("arms", "cube", lambda _: sections.ARMS(patterns.cube))
CONE = Preset("arms", "cone", lambda _: sections.ARMS(patterns.cone))

HOT_FIRE = Preset("body", "hot_fire", lambda _: sections.BODY(patterns.fire))
COLD_FIRE = Preset("body", "cold_fire", lambda _: sections.BODY(patterns.fire2))

CIRCUIT = Preset("body", "circuit", lambda _: circuit.CIRCUIT(patterns.circuit))