from util import color

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
from patterns.flip import Flip

cube = Solid(
    color.magenta
)
cone = Solid(
    color.Color(255, 64, 0)
)
breathe = Breathe(
    Solid(
        color.blue
    )
)
worms = Moving(
    Scaled(
        Hybrid(
            Solid(color.Color(127, 127, 127)),
            Solid(color.Color(0, 0, 10))
        ),
        1/4
    ),
    speed=3/4,
    floor=True
)
noise_rain = Rain(
    Memory(
        Noise(value=0.7, saturation=1)
    )
)
slow_rainbow = Moving(
    Scaled(
        Rainbow(),
        1/2
    ),
    speed=1
)
rainbow = Moving(
    Scaled(
        Rainbow(),
        1/2
    ),
    speed=3/2
)
whole_rainbow = Just(
    Moving(
        Rainbow(),
        1/4
    )
)
rainbow_snakes = Moving(
    Scaled(
        Hybrid(
            Rainbow(),
            Solid(color.black)
        ),
        1/4
    ),
    floor=True
)
rainbow_snakes2 = Moving(
    Scaled(
        Hybrid(
            Moving(
                Rainbow(),
                speed=-1/3
                * 2  # from hybrid
                * 4  # from scaled
            ),
            Solid(color.black)
        ),
        1/4
    ),
    floor=True
)
rainbow_rain = Rain(
    Moving(
        Rainbow()
    )
)
fire = Timed(
    Smooth(
        Memory(
            Sample(
                Gradient(color.yellow, color.Color(255, 64, 0), color.Color(
                    255, 64, 0), color.Color(255, 64, 0), color.red)
            )
        ),
        time=1/16
    ),
    frequency=16
)
fire2 = Timed(
    Smooth(
        Memory(
            Sample(
                Gradient(color.blue.multiply(0.75),
                         color.green.multiply(0.75))
            )
        ),
        time=1/16
    ),
    frequency=16
)
circuit = Flip(
    Moving(
        Scaled(
            Hybrid(
                Solid(color.blue),
                Solid(color.black)
            ),
            1/4
        ),
        floor=True
    )
)

debug_five = Conditional(
    lambda pos: (pos.ipos % 5) == 0, Gradient(color.red, color.blue)
)

none = Solid(color.black)
solid_red = Solid(color.red)
solid_yellow = Solid(color.yellow)
solid_green = Solid(color.green)
solid_cyan = Solid(color.cyan)
solid_blue = Solid(color.blue)
solid_magenta = Solid(color.magenta)
solid_white = Solid(color.white)

pride_flag = lambda *colors: Hybrid(*[Solid(col) for col in colors])