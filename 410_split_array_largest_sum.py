from typing import List
Dynamic programing


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def get_dp(lens, divs):
            for i in range(lens):
                dp[lens][divs] = min(dp[lens][divs], max(
                    dp[i][divs - 1], dp[lens][0] - dp[i][0]))
        n = len(nums)
        dp = [[float('inf')]*m for _ in range(n)]
        # populate first row
        tot = 0
        for i, num in enumerate(nums):
            tot += num
            dp[i][0] = tot

        for divs in range(1, m):  # obviously you divied into divs + 1
            for lens in range(1, n):  # like wise, for index lens you have lens + 1 element
                if divs <= lens:
                    get_dp(lens, divs)
        return dp[n - 1][m - 1]


# Binary search the max and min has to be the total sum and the largest element in the array.
# Binary search the answer. For each mid, find a valid cut to ensure the sub sum is not larger than
# mid and also count the number of arrays. If the count > m, then we can set the upper limit to mid - 1


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = nums[0], 0
        for i in nums:
            r += i
            if i > l:
                l = i
        ans = r
        while r >= l:
            mid = l + (r - l)//2
            count = 1
            sm = 0
            for i in nums:
                if sm + i > mid:
                    sm = i
                    count += 1
                else:
                    sm += i
            if m >= count:
                r = mid - 1
                # Gotta renew the answer here since mid - 1 might be too small in the next iteration`.
                ans = min(ans, mid)
            elif m < count:
                l = mid + 1
        return ans


test = [2, 3, 1, 1, 1, 1, 1]
m = 5
ans = Solution()
ans.splitArray(test, m)
