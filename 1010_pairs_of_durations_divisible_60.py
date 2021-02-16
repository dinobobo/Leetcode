from typing import List
from collections import Counter


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remain = list(map(lambda x: x % 60, time))
        freq = Counter(remain)
        ans = 0
        for t in remain:
            if not t:
                ans += freq[t]
            else:
                if 60 - t in freq:
                    ans += freq[60 - t]
        ans -= freq[30]
        ans -= freq[0]
        return ans // 2


test = [30, 20, 150, 100, 40]
ans = Solution()
ans.numPairsDivisibleBy60(test)
