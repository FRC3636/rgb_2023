class Part:
    # exclusive of upper bound
    def __init__(self, name, start, end):
        self.name = name
        self.start, self.end = start, end
        self.range = (start, end)

    def length(self):
        return self.end - self.start
