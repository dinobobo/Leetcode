# Sliding window. The fast pointer goes to find zeros, until two are found. If there
# are two zeros, the slow pointer can moved pass the first zero, since there won't
# be any subarray that has longer consective ones. The way to understand this problem is
# looking at how many zeros are in the window, and only when there are less than two zeros
# the sub array is valid.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_len = 0
        prev_zero = -1
        while right < len(nums):
            if nums[right] != 0:
                max_len = max(max_len, right - left + 1)
            else:
                if prev_zero == -1:
                    max_len = right - left + 1
                else:
                    max_len = max(max_len, right - left)
                    left = prev_zero + 1
                prev_zero = right
            right += 1
        return max_len


# We can also do a two pass approach. Fast pointer go ahead until there are two zeros, the slow
# pointer will go until it finds a zero. Implement here next round?
