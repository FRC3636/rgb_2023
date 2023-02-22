from colour import Color

def _lerp(a, b, t):
    return a + (b - a) * t

def blend(c1, c2, t):
    r = _lerp(c1.red, c2.red, t)
    g = _lerp(c1.green, c2.green, t)
    b = _lerp(c1.blue, c2.blue, t)
    return Color( rgb = (r, g, b) )