from default import parts

class _FakeModule:
    def __getattr__(*args, **kwargs):
        return None

board = _FakeModule()
neopixel = _FakeModule()

class _FakeNeoPixel(list):
    def fill(self, item):
        for i, _ in enumerate(self):
            self[i] = item
    
    def show(self):
        pass

_strip = _FakeNeoPixel(range(parts.NUM_LEDS))
_strip.fill((0, 0, 0))

neopixel.NeoPixel = lambda *args, **kwargs: _strip