from colour import Color

from patterns.rainbow import RainbowPattern
from patterns.moving import MovingPattern
from patterns.solid import SolidPattern
from patterns.hybrid import HybridPattern
from patterns.scale import ScaledPattern
from patterns.breathe import BreathePattern

class Settings:
    def __init__(self):
        self.presets = {
            "cube": MovingPattern(
                ScaledPattern(
                    HybridPattern(
                        SolidPattern(
                            Color("black")
                        ),
                        SolidPattern(
                            Color("magenta")
                        )
                    ),
                    0.5
                )
            ),
            "cone": MovingPattern(
                ScaledPattern(
                    HybridPattern(
                        SolidPattern(
                            Color("black")
                        ),
                        SolidPattern(
                            Color(
                                rgb = (1, 0.25, 0)
                            )
                        )
                    ),
                    0.25
                )
            ),
            "resting": BreathePattern(
                SolidPattern(
                    Color("blue")
                )
            ),
            "rainbow": MovingPattern(
                ScaledPattern(
                    RainbowPattern(),
                    1/2
                )
            )
        }
        self.properties = {
            "enabled": True,
            "presetId": "rainbow"
        }

    def getPattern(self):
        return self.presets[self.properties["presetId"]]

    def update(self, nwtable):
        for k, v in self.properties.items():
            self.properties[k] = nwtable.getValue(k, v)

    def push(self, nwtable):
        for k, v in self.properties.items():
            nwtable.putValue(k, v)
