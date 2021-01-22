from typing import List
# Divide and conquer. Use sort of merge sort to combine the results


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        def helper(l, r):
            if l == r - 1:
                x1, x2, h = buildings[l]
                return [[x1, h], [x2, 0]]

            mid = l + (r - l)//2
            left_line = helper(l, mid)
            right_line = helper(mid, r)

            left_len = len(left_line)
            right_len = len(right_line)
            left = 0
            right = 0
            curr_h = 0
            left_h = 0
            right_h = 0
            line = []
            while left < left_len and right < right_len:
                if left_line[left][0] < right_line[right][0]:
                    x, left_h = left_line[left]
                    left += 1
                elif left_line[left][0] == right_line[right][0]:
                    x, left_h = left_line[left]
                    right_h = right_line[right][1]
                    left += 1
                    right += 1
                else:
                    x, right_h = right_line[right]
                    right += 1
                if max(left_h, right_h) == curr_h:
                    continue
                else:
                    curr_h = max(left_h, right_h)
                line.append([x, curr_h])
            line += left_line[left:]
            line += right_line[right:]
            return line
        return helper(0, len(buildings))
