# Because 1 <= num <= len(nums), we can parse the array and mark the number on the index
#  == num negative. This basically helps us to track the numbers already exist without
# using a dictionary (it's essentially a dictionary). For the second pass, we can find out
# the indices of which num > 0 and the number index + 1 never appeared in the array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
