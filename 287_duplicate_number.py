from typing import List
# Tortoise and Hare


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


test = [3, 1, 3, 4, 2]
ans = Solution()
print(ans.findDuplicate(test))
