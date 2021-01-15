# Recursion with memoirzation. Time limit exceeded.
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = [[None]*2001 for _ in range(len(nums) + 1)]

        def helper(i, target):
            if target > 1000:
                return 0
            if i == len(nums):
                if target == 0:
                    return 1
                else:
                    return 0
            if memo[i][target + 1000] != None:
                return memo[i][target + 1000]
            else:
                pos = helper(i + 1, target - nums[i])
                neg = helper(i + 1, target + nums[i])
            memo[i][target + 1000] = pos + neg
            return pos + neg
        ans = helper(0, S)
        return ans

# Dynamic programming


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        length = len(nums)
        max_sum = sum(nums)
        if len(nums) == 0:
            return 0
        dp = [[0]*(2*max_sum + 1) for _ in range(len(nums))]
        dp[0][nums[0] + max_sum] += 1
        dp[0][-nums[0] + max_sum] += 1
        for i in range(1, length):
            for j, num in enumerate(dp[i - 1]):
                if num != 0:
                    dp[i][j + nums[i]] += num
                    dp[i][j - nums[i]] += num
        if S > max_sum:
            return 0
        else:
            return dp[-1][S + max_sum]


test = [1, 1, 1, 1, 1]
target = 3

solution = Solution()
ans = solution.findTargetSumWays(test, target)
