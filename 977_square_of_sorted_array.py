# Two pointer from both ends and merge to answer
from collections import deque


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = deque([])
        n = len(nums)
        left = 0
        right = n - 1
        while right >= left:
            if nums[left] >= 0:
                ans.extendleft(
                    [nums[i]**2 for i in range(right, left - 1, -1)])
                return ans
            if nums[right] <= 0:
                ans.extendleft([nums[j]**2 for j in range(left, right + 1)])
                return ans
            if nums[left]*(-1) > nums[right]:
                ans.appendleft(nums[left]**2)
                left += 1
            else:
                ans.appendleft(nums[right]**2)
                right -= 1
        return ans
