from colorsys import hsv_to_rgb

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

def hsv(h, s, v):
    color = hsv_to_rgb(h, s, v)
    return Color(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))

def _lerp(a, b, t):
    return a + (b - a) * t

def blend(c1, c2, t):
    r = _lerp(c1.r, c2.r, t)
    g = _lerp(c1.g, c2.g, t)
    b = _lerp(c1.b, c2.b, t)
    return Color(int(r), int(g), int(b))

black = Color(0, 0, 0)
white = Color(255, 255, 255)

red = Color(255, 0, 0)
green = Color(0, 255, 0)
blue = Color(0, 0, 255)

magenta = Color(255, 0, 255)
cyan = Color(0, 255, 255)
yellow = Color(255, 255, 0)