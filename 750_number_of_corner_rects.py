from collections import defaultdict

# Memoization
# O(m*n^2)


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        counts = defaultdict(int)
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for row in range(rows):
            for i in range(cols - 1):
                if grid[row][i]:
                    for j in range(i + 1, cols):
                        if grid[row][j]:
                            if (i, j) in counts:
                                ans += counts[(i, j)]
                            counts[(i, j)] += 1
        return ans


# Consider two rows together, if we find n occurances where grid[row][col] = grid[row'][col] = 1
# then the total number of pairs is n(n - 1)/2
# O(n^2*m)
