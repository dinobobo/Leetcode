from typing import List
# Just do swaps... with backtracking.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def back_track(start):
            if start == len(nums) - 1:
                ans.append(nums[:])
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                back_track(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
        ans = []
        back_track(0)
        return ans


ans = Solution()
test = [1, 2, 3]
print(ans.permute(test))
