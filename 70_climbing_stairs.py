# Recursive
class Solution:
    def __init__(self):
        self.visited = {}

    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        ans = 0
        if n - 1 in self.visited:
            one_ways = self.visited[n - 1]
        else:
            one_ways = self.climbStairs(n - 1)
        if n - 2 in self.visited:
            two_ways = self.visited[n - 2]
        else:
            two_ways = self.climbStairs(n - 2)
        self.visited[n] = one_ways + two_ways
        return one_ways + two_ways

# DP?
