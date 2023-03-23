from util import color

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
from patterns.translate import Translated

def _update(a, b):
    updated = False
    for k in b:
        if b[k] != a.get(k):
            updated = True
    a.update(b)
    return updated

class Settings:
    def __init__(self, sections):
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
                1.3
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
                1.3
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
            "none": Solid(color.black),
            "solid_red": Solid(color.red),
            "solid_yellow": Solid(color.yellow),
            "solid_green": Solid(color.green),
            "solid_cyan": Solid(color.cyan),
            "solid_blue": Solid(color.blue),
            "solid_magenta": Solid(color.magenta),
            "solid_white": Solid(color.white),
            "transrights": Solid(color.black)
        }
        self.sections = sections

        self.properties = {
            "enabled": True
        }
        for section in self.sections.all_sections.values():
            self.properties[section.name] = None
        
        self.gameinfo = {
            "stage": None,
            "alliance": None,
            "piece": None,
            "matchtype": None,
            "time": None,
            "estopped": None
        }
        self.update_pattern()

    def update_pattern(self):
        self.sections.set_preset("none")

        stage = self.gameinfo.get("stage")
        piece = self.gameinfo.get("piece")
        estopped = self.gameinfo.get("estopped")

        if stage == None:
            self.sections.get_section("body").set_preset("solid_blue")
        else:
            self.sections.get_section("body").set_preset("whole_rainbow")
        
        if estopped:
            self.sections.get_section("body").set_preset("solid_red")
        elif stage == "disabled":
            self.sections.get_section("body").set_preset("rainbow")
        elif piece == "cube":
            self.sections.get_section("arm").set_preset("cube")
        elif piece == "cone":
            self.sections.get_section("arm").set_preset("cone")
        
        for section in self.sections.all_sections.values():
            val = self.properties[section.name]
            if val != None:
                section.set_preset(val)

        self.pattern = self.sections.pattern(self.presets)

    def get_pattern(self):
        return self.pattern

    def update(self, lights, gameinfo):
        new_props = {}
        new_info = {}
        for k, v in self.properties.items():
            new_props[k] = lights.getValue(k, v)
        for k, v in self.gameinfo.items():
            new_info[k] = gameinfo.getValue(k, v)
        props_updated = new_props != self.properties
        info_updated = new_info != self.gameinfo

        self.properties = new_props
        self.gameinfo = new_info

        if info_updated or props_updated:
            self.update_pattern()

    def push(self, nwtable):
        for k, v in self.properties.items():
            if v != None:
                nwtable.putValue(k, v)