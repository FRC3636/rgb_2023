from bisect import bisect_right as bisect


class Range:
    def __init__(self, *ranges):
        self.ranges = list(ranges)
        self.ranges.sort(key=lambda x: x[0])
        self.starts = list(map(lambda x: x[0], self.ranges))

    def get(self, ipos):
        val = bisect(self.starts, ipos) - 1
        range = self.ranges[val]
        if range[0] <= ipos < range[1]:
            return val
        return None

class MappedRange(Range):
    def __init__(self, *items):
        self.items = list(items)
        self.items.sort(key=lambda x: x[0][0])
        super().__init__(*map(lambda x: x[0], items))
    def get(self, ipos):
        val = super().get(ipos)
        if val == None:
            return None
        return self.items[val][1]
