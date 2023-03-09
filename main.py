#!/usr/bin/env python
import board
import neopixel
import time
import ntcore

from settings import Settings
from util.position import Position
from util.range import Range

BRIGHTNESS = 1.0
ORDER = neopixel.GRB
NUM_LEDS = 169
DATA_PIN = board.D18
ADDR = "10.36.36.2"
# ADDR = "10.176.75.34"
DELAY = 1/144
LAYOUT = Range(77, 46, 46)

strip = neopixel.NeoPixel(
    DATA_PIN, NUM_LEDS, pixel_order = ORDER, brightness = BRIGHTNESS, auto_write = False
)

instance = ntcore.NetworkTableInstance.getDefault()
instance.startClient4("lights")
instance.setServer(ADDR)

nwtable = instance.getTable("Lights")

settings = Settings(LAYOUT)
settings.push(nwtable)

# fixes layout of our lights
mapping = lambda pos: pos.translate(7)

frame = 0
while True:
    settings.update(nwtable)
    pattern = settings.get_pattern()
    if settings.properties["enabled"] and pattern != None:
        for i in range(NUM_LEDS):
            pos = mapping(Position(i, NUM_LEDS))
            color = pattern.at(pos)
            strip[i] = (color.r, color.g, color.b)
        pattern.fullupdate(DELAY, frame)
    else:
        strip.fill((0, 0, 0))
    strip.show()
    time.sleep(DELAY)
    frame += 1
    frame %= 1_000_000