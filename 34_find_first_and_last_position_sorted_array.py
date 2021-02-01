# Generic binary search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_num(l, r):
            while l <= r:
                mid = (l + r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        l, r = 0, len(nums) - 1
        idx = find_num(l, r)
        if idx == -1:
            return [-1, -1]
        else:
            lr, rr = idx, idx
            while lr >= 0 and nums[lr] == target:
                lr -= 1
            while rr < len(nums) and nums[rr] == target:
                rr += 1
        return [lr + 1, rr - 1]

# Finding the edge with a modified binary search. You essentially add = in to the
# decision making instead of returning. Then find the first value samller than target
# and the first value larger than target.


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_num(l, r, is_left):
            while l <= r:
                mid = (l + r)//2
                if nums[mid] > target or (nums[mid] == target and is_left):
                    r = mid - 1
                else:
                    l = mid + 1
            return r
        if len(nums) == 0:
            return [-1, -1]
        left_edge = find_num(0, len(nums) - 1, True) + 1
        right_edge = find_num(0, len(nums) - 1, False)
        if left_edge == len(nums) or right_edge == -1 or nums[left_edge] != target:
            return [-1, -1]
        else:
            return [left_edge, right_edge]
