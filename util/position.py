import math

class Position:
    def __init__(self, dpos, dtotal):
        self.dpos = dpos % dtotal
        self.ipos = math.ceil(self.dpos)
        self.dtotal = dtotal
        self.total = math.ceil(dtotal)
        self.pos = self.dpos / self.dtotal
    
    def translate(self, amnt):
        return Position(self.dpos + amnt, self.dtotal)
    
    def scale(self, amnt):
        return Position(self.dpos * amnt, self.dtotal)