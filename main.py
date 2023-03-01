#!/usr/bin/env python
import board
import neopixel
import time
import ntcore

from settings import Settings

BRIGHTNESS = 0.1
ORDER = neopixel.GRB
NUM_LEDS = 117
DATA_PIN = board.D18
ADDR = "10.36.36.2"
# ADDR = "192.168.137.1"
DELAY = 1/30

strip = neopixel.NeoPixel(
    DATA_PIN, NUM_LEDS, pixel_order = ORDER, brightness = BRIGHTNESS, auto_write = False
)

instance = ntcore.NetworkTableInstance.getDefault()
instance.startClient4("lights")
instance.setServer(ADDR)

nwtable = instance.getTable("Lights")

settings = Settings()
settings.push(nwtable)

while True:
    settings.update(nwtable)
    pattern = settings.getPattern()
    if settings.properties["enabled"]:
        for i in range(NUM_LEDS):
            color = pattern.at(i / NUM_LEDS)
            strip[i] = (color.r, color.g, color.b)
        pattern.fullupdate(DELAY)
    else:
        strip.fill((0, 0, 0))
    strip.show()
    time.sleep(DELAY)