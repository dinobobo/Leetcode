from math import e, log


class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left = int(e**(0.5 * log(x)))
        right = left + 1
        print(x)
        print(right * right > x)
        return left if right * right > x else right


ans = Solution()
for i in range(2, 100):
    ans.mySqrt(i)
