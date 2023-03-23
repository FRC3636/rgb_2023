from bisect import bisect_right as bisect


class Range:
    def __init__(self, *ranges):
        self.ranges = list(ranges)
        self.ranges.sort(key=lambda x: x[0])
        self.starts = list(map(lambda x: x[0], self.ranges))

    def get(self, ipos):
        return bisect(self.starts, ipos) - 1


class MappedRange(Range):
    def __init__(self, *items):
        super().__init__(*map(lambda x: x[0], items))
        self.items = items

    def get(self, ipos):
        val = super().get(ipos)
        return self.items[val][1]
