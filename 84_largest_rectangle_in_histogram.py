from math import log2, ceil
from typing import List
# Generic divide and conquer.
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         def helper(l, r):
#             if l == r:
#                 return 0
#             min_idx = find_min(l, r)
#             left_max = helper(l, min_idx)
#             right_max = helper(min_idx + 1, r)
#             mid_max = heights[min_idx] * (r - l)
#             return max(left_max, right_max, mid_max)

#         def find_min(l, r):
#             curr_min = l
#             for i in range(l, r):
#                 if heights[i] < heights[curr_min]:
#                     curr_min = i
#             return curr_min

#         return helper(0, len(heights))


# Use Segment tree to find min.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        seg_tree = self.construct_min_seg_idx(heights, len(heights))

        def helper(l, r):
            if l == r:
                return 0
            min_idx = self.get_min_idx(
                l, r, 0, len(heights), 0, seg_tree, heights)
            print(min_idx)
            left_max = helper(l, min_idx)
            right_max = helper(min_idx + 1, r)
            mid_max = heights[min_idx] * (r - l)
            return max(left_max, right_max, mid_max)
        return helper(0, len(heights))

    def construct_min_seg_idx(self, arr, n):
        x = int((ceil(log2(n))))
        max_size = 2**(x + 1) - 1
        segtree = [0] * max_size
        self.min_seg_idx(arr, 0, n, segtree, 0)
        return segtree

    def min_seg_idx(self, arr, l, r, segtree, curr):
        if l == r - 1:
            segtree[curr] = l
        else:
            mid = l + (r - l) // 2
            left_idx = self.min_seg_idx(arr, l, mid, segtree, curr*2 + 1)
            right_idx = self.min_seg_idx(arr, mid, r, segtree, curr*2 + 2)
            if arr[left_idx] < arr[right_idx]:
                segtree[curr] = left_idx
            else:
                segtree[curr] = right_idx
        return segtree[curr]

    def get_min_idx(self, l, r, arr_l, arr_r, curr, segtree, arr):
        if arr_l >= r or arr_r <= l:
            return -1
        elif arr_l >= l and arr_r <= r:
            return segtree[curr]
        else:
            mid = arr_l + (arr_r - arr_l)//2
            left_idx = self.get_min_idx(
                l, r, arr_l, mid, curr*2 + 1, segtree, arr)
            right_idx = self.get_min_idx(
                l, r, mid, arr_r, curr*2 + 2, segtree, arr)
            if right_idx == -1:
                return left_idx
            if left_idx == -1:
                return right_idx
            if arr[right_idx] > arr[left_idx]:
                return left_idx
            else:
                return right_idx


heights = [2, 1, 5, 6, 2, 3]
solution = Solution()
solution.largestRectangleArea(heights)
