from collections import deque

# Keep the deque in decreasing order, so that tha max is always on the left
# Whenever add a new element in, pop the numbers that are smaller than it
# and the index that is out of range.


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def clean_deque(i):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

        # Initialize
        ans = []
        dq = deque()
        for i in range(k):
            clean_deque(i)
            dq.append(i)
        ans.append(nums[dq[0]])
        for i in range(k, len(nums)):
            clean_deque(i)
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans


# Use Dynamic programming. Think about divide the array into cells with k length.
# What is the max when the window overlaps with two cells?
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left_max = []
        right_max = []
        for i in range(0, len(nums), k):
            k1 = min(k, len(nums) - i)
            lm = nums[i]
            rm = nums[i + k1 - 1]
            temp_right = []
            for j in range(k1):
                lm = max(lm, nums[j + i])
                left_max.append(lm)
                rm = max(rm, nums[i + k1 - 1 - j])
                temp_right.append(rm)
            right_max += temp_right[::-1]
        return [max(right_max[i], left_max[i + k - 1]) for i in range(len(nums) - k + 1)]
