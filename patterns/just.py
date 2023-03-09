from patterns.manipulate import Manipulated
from util.position import Position

Just = lambda inner, point = 0: Manipulated(inner, lambda pos: Position(point, pos.total))