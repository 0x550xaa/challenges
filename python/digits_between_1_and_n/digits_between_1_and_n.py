class Problem:
    def __init__(self, n):
        self.n = n

    def solve(self):
        i = 0
        for x in range(1, self.n):
            i += len(str(x))
        return i
