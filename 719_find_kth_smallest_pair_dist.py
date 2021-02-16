class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = l + (r - l) // 2
            pairs = self.find_pairs(mid, nums)
            if pairs < k:
                l = mid + 1
            else:
                r = mid
        return l

    def find_pairs(self, d, nums):
        # find number of pairs that has dist <= d using DP
        # i and j are indices in nums that satifies nums[j] is the smallest number that satisfies nums[j] - nums[i] > d
        # loop through 0, len(nums) - 2 and use dp relation
        # dp[i] = dp[i - 1] + j - i - 1 and dp[i] represents the total number of pairs that has the left indices from 0 to i
        # It is essentially because evey time you increment i, you gain j - i - 1 new pairs
        count = 0
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] <= nums[i] + d:
                j += 1
            count += j - i - 1
        return count
