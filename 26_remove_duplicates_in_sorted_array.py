# Two pointer. Fast pointer keeps going until the element it's
# pointing to is different from the element the slow pointer is pointing to
# then move this value to i + 1 location
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
        return i + 1
