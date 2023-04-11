#!/usr/bin/env python
import os
import time

if not os.environ.get("RGB_SIM") == "true":
    import board
    import neopixel
    ADDR = "10.36.36.2"
else:
    from simulation import board
    from simulation import neopixel
    ADDR = "127.0.0.1"

if not os.environ.get("RGB_NT_SIM") == "true":
    import ntcore
else:
    from simulation import ntcore

from settings import Settings
from util.position import Position
from default.parts import NUM_LEDS

BRIGHTNESS = 0.5
ORDER = neopixel.GRB
DATA_PIN = board.D18
DELAY = 1/60

strip = neopixel.NeoPixel(
    DATA_PIN, NUM_LEDS, pixel_order = ORDER, brightness = BRIGHTNESS, auto_write = False
)

instance = ntcore.NetworkTableInstance.getDefault()
instance.setServer(ADDR)
instance.startClient4("lights")

lights = instance.getTable("Lights")
gameinfo = instance.getTable("GameInfo")

settings = Settings()
settings.push(lights)

strip.fill((0, 0, 0))
def update(dt, frame):
    settings.update(lights, gameinfo)
    pattern = settings.get_pattern()
    if settings.properties["enabled"] and pattern != None:
        for i in range(NUM_LEDS):
            pos = Position(i, NUM_LEDS)
            color = pattern.at(pos)
            strip[i] = (color.r, color.g, color.b)
        pattern.fullupdate(dt, frame)
    else:
        strip.fill((0, 0, 0))
    strip.show()

if __name__ == "__main__":
    dt = 0
    frame = 0
    while True:
        prev = time.time()
        update(dt)
        time.sleep(DELAY)
        dt = time.time() - prev
        frame += 1
        frame %= 1_000_000