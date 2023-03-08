from patterns.pattern import Pattern
from patterns.solid import Solid
from util import color

class Conditional(Pattern):
	def __init__(self, condition, on = Solid(color.white), off = Solid(color.black)):
		super().__init__()
		self.add_child(on)
		self.add_child(off)
		self.on = on
		self.off = off
		self.condition = condition
	
	def at(self, pos):
		if self.condition(pos):
			return self.on.at(pos)
		else:
			return self.off.at(pos)