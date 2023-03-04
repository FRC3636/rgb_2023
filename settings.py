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

class Settings:
    def __init__(self):
        self.presets = {
            "cube": Moving(
                Scaled(
                    Hybrid(
                        Solid(
                            color.black
                        ),
                        Solid(
                            color.magenta
                        )
                    ),
                    1/4
                )
            ),
            "cone": Moving(
                Scaled(
                    Hybrid(
                        Solid(
                            color.black
                        ),
                        Solid(
                            color.Color(255, 64, 0)
                        )
                    ),
                    1/4
                )
            ),
            "resting": Breathe(
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
            )
        }
        self.properties = {
            "enabled": True,
            "presetId": "rainbow_snakes2"
        }

    def get_pattern(self):
        return self.presets.get(self.properties["presetId"])

    def update(self, nwtable):
        for k, v in self.properties.items():
            self.properties[k] = nwtable.getValue(k, v)

    def push(self, nwtable):
        for k, v in self.properties.items():
            nwtable.putValue(k, v)
