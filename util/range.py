from bisect import bisect_right as bisect

class Range:
    def __init__(self, *lengths):
        self.lengths = list(lengths)
        self.starts = []
        self.ends = []
        total = 0
        for l in lengths:
            self.starts.append(total)
            total += l
            self.ends.append(total)

    def get(self, ipos):
        target = bisect(self.starts, ipos) - 1
        return (target, self.starts[target], self.ends[target])
