from patterns.pattern import SizedPattern
from patterns.solid import Solid
from util import color
import math

class Automata(SizedPattern):
    def __init__(self, pattern = 60, wrapping = False, frequency = 8, on = Solid(color.white), off = Solid(color.black)):
        super().__init__()
        self.rules = {}
        rule = format(pattern, "0>8b")
        for i in range(8):
            self.rules[7 - i] = rule[i] == '1'
        self.wrapping = wrapping
        self.frequency = frequency
        self.time = 0
        self.state = {}
        self.on = on
        self.off = off
        self.add_child(on)
        self.add_child(off)
    
    def new_size(self, size):
        self.state.clear()
        for i in range(size):
            self.state[i] = False
        self.state[math.floor(size / 2)] = True
    
    def at(self, pos):
        super().at(pos)
        if self.state[pos.ipos]:
            return self.on.at(pos)
        return self.off.at(pos)

    def step(self):
        new_state = {}
        for i in range(self.remembered):
            n = 0
            left = i - 1
            right = i + 1
            if self.wrapping:
                left %= self.remembered
                right %= self.remembered
            if left >= 0 and self.state[left]:
                n += 1
            if self.state[i]:
                n += 2
            if right < self.remembered and self.state[right]:
                n += 4
            new_state[i] = self.rules[n]
        self.state = new_state

    def update(self, dt, frame):
        self.time += dt
        while self.time >= 1 / self.frequency:
            self.time -= 1 / self.frequency
            if self.remembered != None:
                self.step()