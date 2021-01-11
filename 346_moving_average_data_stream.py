from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.count = 0
        self.q = deque([])

    def next(self, val: int) -> float:
        if self.count < self.size:
            self.q.append(val)
            self.count += 1
            return sum(self.q)/self.count
        else:
            self.q.popleft()
            self.q.append(val)
            return sum(self.q)/self.size


# You don't even need to pop the elements, since it won't affect the
# average outcome.

# Also keep track of the sum so that we only need to operations to find
# the average.
