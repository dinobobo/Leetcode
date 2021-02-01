# DFS with memoization
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        visited = {}

        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return grid[m - 1][n - 1]
            if (row, col) in visited:
                return visited[(row, col)]
            bot = dfs(row + 1, col) if row != m - 1 else float('inf')
            right = dfs(row, col + 1) if col != n - 1 else float('inf')
            total = min(bot, right) + grid[row][col]
            visited[(row, col)] = total
            return total

        m = len(grid)
        n = len(grid[0])
        return dfs(0, 0)


# Dynamic programing
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
       # dp dp[i][j - 1] = min(dp[i + 1][j - 1] + dp[i][j])
        m, n = len(grid), len(grid[0])
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row < m - 1 and col < n - 1:
                    grid[row][col] += min(grid[row + 1]
                                          [col], grid[row][col + 1])
                elif row < m - 1 and col == n - 1:
                    grid[row][col] += grid[row + 1][col]
                elif row == m - 1 and col < n - 1:
                    grid[row][col] += grid[row][col + 1]
        return grid[0][0]
