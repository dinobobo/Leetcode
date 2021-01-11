from collections import deque


# BFS
class Solution:
    LAND = '1'
    WATER = '0'
    D = [0, 1, 0, -1, 0]

    def numIslands(self, grid) -> int:
        num = 0
        m = len(grid)
        n = len(grid[0])
        lands = []
        for row in range(m):
            for col in range(n):
                if grid[row][col] == self.LAND:
                    lands.append([row, col])
        while len(lands) > 0:
            i, j = lands.pop()
            if grid[i][j] == self.LAND:
                island = deque([[i, j]])
                while len(island) > 0:
                    area = len(island)
                    for _ in range(area):
                        land = island.pop()
                        grid[land[0]][land[1]] = '2'
                        for i in range(4):
                            p, q = land[0] + self.D[i], land[1] + self.D[i + 1]
                            if 0 <= p < m and 0 <= q <= n and grid[p][q] == self.LAND:
                                grid[p][q] = '2'
                                island.appendleft([p, q])
                num += 1
        return num

# DFS?


# Union find?


test = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
solution = Solution()
ans = solution.numIslands(test)
