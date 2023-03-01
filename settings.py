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
                    0.5
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
                    0.25
                )
            ),
            "resting": Breathe(
                Solid(
                    color.blue
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
                    0.25
                )
            )
        }
        self.properties = {
            "enabled": True,
            "presetId": "whole_rainbow"
        }

    def getPattern(self):
        return self.presets[self.properties["presetId"]]

    def update(self, nwtable):
        for k, v in self.properties.items():
            self.properties[k] = nwtable.getValue(k, v)

    def push(self, nwtable):
        for k, v in self.properties.items():
            nwtable.putValue(k, v)
