from colorsys import hsv_to_rgb
from colormath.color_objects import sRGBColor, LCHabColor
from colormath.color_conversions import convert_color

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def multiply(self, scale):
        return Color(int(self.r * scale), int(self.g * scale), int(self.b * scale))
    
    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b})"

def hsv(h, s, v):
    color = hsv_to_rgb(h, s, v)
    return Color(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))

def lch(l, c, h):
    color = convert_color(LCHabColor(l, c, h), sRGBColor)
    return Color(int(color.clamped_rgb_r * 255), int(color.clamped_rgb_g * 255), int(color.clamped_rgb_b * 255))

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