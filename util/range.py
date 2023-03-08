from bisect import bisect_right as bisect

class Range:
    def __init__(self, *items):
        self.items = list(items)
        self.starts = []
        self.ends = []
        self.total = 0
        for item in items:
            self.starts.append(self.total)
            self.total += item[1]
            self.ends.append(self.total)

    def get(self, ipos):
        target = bisect(self.starts, ipos) - 1
        return (self.items[target][0], self.starts[target], self.ends[target])

