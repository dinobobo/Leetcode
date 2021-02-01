from collections import defaultdict
from typing import List


class Solution:

    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Remove lamp function
        def remove_lamp(row, col):
            rows[row] -= 1
            cols[col] -= 1
            diags[row - col] -= 1
            antidiags[row + col] -= 1
            lamp_set.remove((row, col))

        # Check illumination and boundary

        def is_illumed(row, col):
            return 0 <= row < N and 0 <= col < N and \
                rows[row] > 0 or cols[col] > 0 or \
                diags[row - col] > 0 or antidiags[row + col] > 0

        # Make dic for lighted area
        rows = defaultdict(int)
        cols = defaultdict(int)
        diags = defaultdict(int)
        antidiags = defaultdict(int)
        lamp_set = set()
        for lamp in lamps:
            row, col = lamp
            rows[row] += 1
            cols[col] += 1
            diags[row - col] += 1
            antidiags[row + col] += 1
            lamp_set.add((row, col))

        ans = []

        # Check illumination
        d = (1, 0, -1)
        for query in queries:
            row, col = query
            if is_illumed(row, col):
                ans.append(1)
            else:
                ans.append(0)

        # Turn off neighbor lamps
            for i in d:
                for j in d:
                    if (row + i, col + j) in lamp_set:
                        remove_lamp(row + i, col + j)
        return ans


lamps = [[7, 55], [53, 61], [2, 82], [67, 85], [81, 75], [38, 91], [68, 0], [60, 43], [40, 19], [12, 75], [26, 2], [24, 89], [42, 81], [60, 58], [77, 72], [33, 24], [19, 93], [7, 16],
         [58, 54], [78, 57], [97, 49], [65, 16], [42, 75], [90, 50], [89, 34], [76, 97], [58, 23], [
             62, 47], [94, 28], [88, 65], [3, 87], [81, 10], [12, 81], [44, 81], [54, 92], [90, 54], [17, 54],
         [27, 82], [48, 15], [8, 46], [4, 99], [15, 13], [90, 77], [2, 87], [18, 33], [52, 90], [4, 95], [
             57, 61], [31, 22], [32, 8], [49, 26], [24, 65], [88, 55], [88, 38], [64, 76], [94, 76],
         [59, 12], [41, 46], [80, 28], [38, 36], [65, 67], [75, 37], [56, 97], [83, 57], [2, 4], [
    44, 43], [71, 90], [62, 40], [79, 94], [81, 11], [96, 34], [38, 11], [22, 3], [54, 96], [78, 33],
    [54, 54], [79, 98], [1, 28], [0, 32], [37, 11]]

queries = [[24, 84], [95, 68], [80, 35], [31, 53], [69, 45], [85, 29], [87, 25], [42, 47], [7, 59], [99, 3], [31, 70], [64, 62], [44, 91], [55, 25], [15, 52], [95, 33], [21, 29],
           [61, 34], [93, 34], [79, 27], [30, 86], [52, 0], [18, 10], [5, 1], [40, 21], [11, 48], [
               55, 94], [22, 42], [81, 0], [39, 43], [5, 25], [43, 29], [45, 47], [83, 93], [77, 70], [22, 63],
           [30, 73], [18, 48], [39, 88], [91, 47]]

N = 100
ans = Solution()
ans.gridIllumination(N, lamps, queries)


# Use arrays to represent cols, rows, and diagnals.
