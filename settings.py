from util import color
from util.range import Range

from patterns.rainbow import Rainbow
from patterns.moving import Moving
from patterns.solid import Solid
from patterns.hybrid import Hybrid
from patterns.scale import Scaled
from patterns.breathe import Breathe
from patterns.cycle import Cycle
from patterns.gradient import Gradient
from patterns.just import Just
from patterns.noise import Noise
from patterns.memory import Memory
from patterns.rain import Rain
from patterns.choice import Choice
from patterns.timed import Timed
from patterns.smooth import Smooth
from patterns.sample import Sample
from patterns.automata import Automata
from patterns.conditional import Conditional
from patterns.ranged import Ranged
from patterns.flip import Flip

class Settings:
    def __init__(self, layout):
        self.presets = {
            "cube": Moving(
                Scaled(
                    Hybrid(
                        Solid(
                            color.magenta.multiply(0.02)
                        ),
                        Solid(
                            color.magenta
                        )
                    ),
                    1/2
                ),
                1
            ),
            "cone": Moving(
                Scaled(
                    Hybrid(
                        Solid(
                            color.Color(255, 64, 0).multiply(0.02)
                        ),
                        Solid(
                            color.Color(255, 64, 0)
                        )
                    ),
                    1/2
                ),
                1
            ),
            "breathe": Breathe(
                Solid(
                    color.blue
                )
            ),
            "worms": Moving(
                Scaled(
                    Hybrid(
                        Solid(color.Color(127, 127, 127)),
                        Solid(color.Color(0, 0, 10))
                    ),
                    1/4
                ),
                speed = 3/4
            ),
            "noise_rain": Rain(
                Memory(
                    Noise(value = 0.7, saturation = 1)
                )
            ),
            "rainbow": Moving(
                Scaled(
                    Rainbow(),
                    1/2
                )
            ),
            "whole_rainbow": Just(
                Moving(
                    Rainbow(),
                    1/4
                )
            ),
            "rainbow_snakes":
            Moving(
                Scaled(
                    Hybrid(
                        Rainbow(),
                        Solid(color.black)
                    ),
                    1/4
                )
            ),
            "rainbow_snakes2": Moving(
                Scaled(
                    Hybrid(
                        Moving(
                            Rainbow(),
                            speed = -1/3
                                * 2 # from hybrid
                                * 4 # from scaled
                        ),
                        Solid(color.black)
                    ),
                    1/4
                )
            ),
            "rainbow_rain": Rain(
                Moving(
                    Rainbow()
                )
            ),
            "fire": Timed(
                Smooth(
                    Memory(
                        Sample(
                            Gradient(color.yellow, color.Color(255, 64, 0), color.Color(255, 64, 0), color.Color(255, 64, 0), color.red)
                        )
                    ),
                    time = 1/16
                ),
                frequency = 16
            ),
            "fire2": Timed(
                Smooth(
                    Memory(
                        Sample(
                            Gradient(color.blue.multiply(0.75), color.green.multiply(0.75))
                        )
                    ),
                    time = 1/16
                ),
                frequency = 16
            ),
            "debug_five": Conditional(
                lambda pos: (pos.ipos % 5) == 0, Gradient(color.red, color.blue)
            ),
            "debug_white": Solid(color.white)
        }
        self.properties = {
            "enabled": True,
            "section_mode": True,
            "body_section": "whole_rainbow",
            "arm_section": "cube",
            "flip_section": 2,
            "default_pattern": "fire2"
        }
        self.sections = [None, None, None]
        self.update_sections()
        self.pattern = Ranged(layout, self.sections)

    def update_sections(self):
        self.sections[0] = self.presets.get(self.properties["body_section"])
        self.sections[1] = self.presets.get(self.properties["arm_section"])
        self.sections[2] = self.sections[1]
        flip = self.properties["flip_section"]
        if flip != -1:
            self.sections[flip] = Flip(self.sections[flip])

    def get_pattern(self):
        if self.properties["section_mode"]:
            return self.pattern
        return self.presets.get(self.properties["default_pattern"])

    def update(self, nwtable):
        new_props = {}
        for k, v in self.properties.items():
            new_props[k] = nwtable.getValue(k, v)
        updated = new_props != self.properties
        self.properties = new_props
        if updated:
            self.update_sections()

    def push(self, nwtable):
        for k, v in self.properties.items():
            nwtable.putValue(k, v)
