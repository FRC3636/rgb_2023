class Part:
    # exclusive of upper bound
    def __init__(self, start, end):
        self.start, self.end = start, end

    def length(self):
        return self.end - self.start
