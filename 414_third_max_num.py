# Use a set to contain the three largest numbers. Add in new numbers in and
# pop out the min if len > 3.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_set = set()
        for num in nums:
            max_set.add(num)
            if len(max_set) > 3:
                max_set.remove(min(max_set))
        return max(max_set) if len(max_set) < 3 else min(max_set)
