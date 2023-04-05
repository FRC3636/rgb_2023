from util import color
from util.section import Layout, Section, Part, PartTransform
from default import *

from patterns.rainbow import Rainbow
from patterns.moving import Moving
from patterns.solid import Solid
from patterns.hybrid import Hybrid
from patterns.scale import Scaled, ScaledTo
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

def _update(a, b):
    updated = False
    for k in b:
        if b[k] != a.get(k):
            updated = True
    a.update(b)
    return updated

class Settings:
    def __init__(self):
        self.presets = {
            "cube": Solid(
                 color.magenta
	    ),
            "cone": Solid(
                color.Color(255, 64, 0)
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
            "armrainbow": Just(
                Moving(
                    Gradient(color.red, color.yellow, color.green, color.cyan, color.magenta, color.red),
                    1/4
                )
            ),
            "armrainbow2": Just(
                Moving(
                    Gradient(color.red, color.yellow, color.green, color.cyan, color.magenta, color.red),
                    1/4
                ),
                7
            )
        }

        self.properties = {
            "enabled": True
        }
        
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
        stage = self.gameinfo.get("stage")
        piece = self.gameinfo.get("piece")
        estopped = self.gameinfo.get("estopped")
        alliance = self.gameinfo.get("alliance")

        layout = None

        if stage == None:
            layout = Layout(
                Section(
                    self.presets["solid_blue"],
                    Part(EVERYTHING)
                )
            )
        elif estopped:
            layout = Layout(
                Section(
                    self.presets["solid_red"],
                    Part(EVERYTHING)
                )
            )
        else:
            body_pattern = "whole_rainbow"
            uarm_pattern = "armrainbow"
            darm_pattern = "armrainbow2"
            panel_pattern = "whole_rainbow"
            
            # if alliance == "red":
            #     body_pattern = "solid_red"
            # elif alliance == "blue":
            #     body_pattern = "solid_blue"
            
            if stage == "teleop":
                uarm_pattern = piece
                darm_pattern = piece
            
            layout = Layout(
                Section(
                    self.presets[body_pattern],
                    Part(BODY1),
                    Part(BODY2),
                    Part(BODY3),
                    Part(BODY4),
                    Part(BODY5),
                    Part(BODY6),
                    Part(BODY7),
                    Part(BODY8),
                    Part(BODY9)
                ),
                Section(
                    self.presets[uarm_pattern],
                    Part(RB_UP),
                    Part(LB_UP)
                ),
                Section(
                    self.presets[darm_pattern],
                    Part(RB_DOWN),
                    Part(LB_DOWN)
                ),
                Section(
                    self.presets[panel_pattern],
                    Part(PANEL)
                )
            )

        self.pattern = layout.pattern()

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
