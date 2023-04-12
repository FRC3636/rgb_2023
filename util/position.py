import math

class Position:
    def __init__(self, dpos, dtotal):
        self.dpos = dpos % dtotal
        self.dtotal = dtotal
        self.total = math.floor(dtotal)
        self.ipos = math.floor(dpos) % self.total
        self.pos = self.dpos / self.dtotal
    
    def translate(self, amnt):
        return Position(self.dpos + amnt, self.dtotal)

    def flip(self):
        return Position(self.dtotal - self.dpos - 1, self.dtotal)
    
    def scale(self, amnt):
        return Position(self.dpos, self.dtotal / amnt)
    
    def floor(self):
        return Position(self.ipos, self.total)