#!/usr/bin/env python
import board
import neopixel
import time
import ntcore

from settings import Settings

BRIGHTNESS = 0.2
ORDER = neopixel.GRB
NUM_LEDS = 117
DATA_PIN = board.D18
ADDR = "10.36.36.2"
# ADDR = "192.168.137.1"
DELAY = 1/50

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
            (r, g, b) = pattern.at(i / NUM_LEDS).rgb
            color = (int(r * 255), int(g * 255), int(b * 255))
            strip[i] = color
        pattern.update(DELAY)
    else:
        strip.fill((0, 0, 0))
    strip.show()
    time.sleep(DELAY)