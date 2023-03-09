from patterns.manipulate import Manipulated

Flip = lambda inner: Manipulated(inner, lambda pos: pos.flip())