# Dynamic programming
# Find the answer from 1 to n.
class Solution:
    def numSquares(self, n: int) -> int:
        sqs = [i**2 for i in range(1, int(n**0.5) + 1)]
        dp = [float('inf')]*(n + 1)
        dp[0] = 0
        for num in range(1, n + 1):
            for sq in sqs:
                if sq <= num:
                    dp[num] = min(dp[num], dp[num - sq] + 1)
        return dp[-1]


# Greedy: check if k of squares works where k ranges from 1 to n.
class Solution:
    def numSquares(self, n: int) -> int:
        sqs = set([i**2 for i in range(1, int(n**0.5) + 1)])
        for k in range(1, n + 1):
            if self.is_divided(n, k, sqs):
                return k

    def is_divided(self, n, count, sqs):
        if count == 1:
            return n in sqs
        else:
            for sq in sqs:
                if sq < n and self.is_divided(n - sq, count - 1, sqs):
                    return True
            return False


# Similar Greedy, but use BFS.
class Solution:
    def numSquares(self, n: int) -> int:
        sqs = set([i**2 for i in range(1, int(n**0.5) + 1)])
        count = 1
        q = set()
        q.add(n)
        while len(q) > 0:
            length = len(q)
            next_q = set()
            for i in range(length):
                remain = q.pop()
                if remain in sqs:
                    return count
                else:
                    for sq in sqs:
                        if sq < remain:
                            next_q.add(remain - sq)
            q = next_q
            count += 1
