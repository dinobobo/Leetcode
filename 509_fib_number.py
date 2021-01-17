# DP
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prev = 0
        curr = 1
        for _ in range(n - 1):
            prev, curr = curr, prev + curr
        return curr
