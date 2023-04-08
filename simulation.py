from default import parts

class _FakeModule:
    def __getattr__(*args, **kwargs):
        return None

class _FakeObj:
    def __getattr__(*args, **kwargs):
        return lambda *args, **kwargs: None

board = _FakeModule()
neopixel = _FakeModule()
ntcore = _FakeModule()

class _FakeNeoPixel(list):
    def fill(self, item):
        for i, _ in enumerate(self):
            self[i] = item
    
    def show(self):
        pass

_strip = _FakeNeoPixel(range(parts.NUM_LEDS))
_strip.fill((0, 0, 0))
neopixel.NeoPixel = lambda *args, **kwargs: _strip

class _FakeNwInstance(_FakeObj):
    def __init__(self):
        self.tables = {}
    
    def getTable(self, key):
        if key in self.tables:
            return self.tables[key]
        self.tables[key] = _FakeNwTable()
        return self.tables[key]
    
    @classmethod
    def getDefault(self):
        return _default_inst

_default_inst = _FakeNwInstance()
ntcore.NetworkTableInstance = _FakeNwInstance

class _FakeNwTable(dict):
    def getValue(self, topic, default):
        return self.get(topic, default)
    
    def putValue(self, topic, value):
        self[topic] = value