class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def is_same(land1, land2):
            if len(land1) != len(land2):
                return False
            diff_row = land1[0][0] - land2[0][0]
            diff_col = land1[0][1] - land2[0][1]
            i = 1
            while i < len(land1):
                if land1[i][0] - land2[i][0] != diff_row or land1[i][1] - land2[i][1] != diff_col:
                    return False
                i += 1
            return True

        def dfs(i, j, island):
            if grid[i][j] != 1:
                return
            else:
                grid[i][j] = 2
                island.append([i, j])
            for k in range(4):
                new_i, new_j = i + d[k], j + d[k + 1]
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                    dfs(new_i, new_j, island)

        d = [0, 1, 0, -1, 0]
        ans = 0
        m, n = len(grid), len(grid[0])

        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island = []
                    dfs(i, j, island)
                    islands.add(
                        frozenset((i[0] - island[0][0], i[1] - island[0][1]) for i in island))
        print(list(islands))
        return len(islands)


# Use the path as the Hash key?
