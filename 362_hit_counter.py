from collections import deque


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = deque()
        self.size = 0

    def clear_hits(self, timestamp):
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
            self.size -= 1

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.clear_hits(timestamp)
        self.hits.append(timestamp)
        self.size += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.clear_hits(timestamp)
        return self.size


# Use an array from 0 to 299. Whenever the wrap around happens, reset the count.
