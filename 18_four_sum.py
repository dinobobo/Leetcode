from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def two_sum(l, r, target):
            ans = []
            while r > l:
                tot = nums[l] + nums[r]
                if tot > target:
                    r -= 1
                elif tot < target:
                    l += 1
                else:
                    ans.append([nums[l], nums[r]])
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        ans.append([nums[l], nums[r]])
                        l += 1
                    while r - 1 > l and nums[r] == nums[r - 1]:
                        ans.append([nums[l], nums[r]])
                        r -= 1
                    l += 1
                    r -= 1
            return ans

        def three_sum(idx, target):
            ans = []
            for i in range(idx, n - 2):
                twos = two_sum(i + 1, n - 1, target - nums[i])
                for k in twos:
                    ans.append([nums[i]] + k)
            return ans
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n - 3):
            for j in three_sum(i + 1, target - nums[i]):
                ans.add(tuple([nums[i]] + j))
        return list(ans)


test = [-4, -3, -2, -1, 0, 0, 1, 2, 3, 4]
target = 0
ans = Solution()
ans.fourSum(test, target)
