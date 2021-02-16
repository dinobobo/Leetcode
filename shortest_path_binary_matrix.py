# Instead of a standart BFS, we use the A* heuristic. The idea is that we explore the node with
# the highest potential (shortest estimated path length). To make sure this approach is correct,
# we explore all the nodes with an estimation of x before any nodes with path length > x

from heapq import heappush, heappop


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # maintain a min heap using estimate as the sort metric
        # keep poping until the grid[n - 1][n - 1] is visited
        # keep a set to track visited nodes
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        visited = set()
        d = [-1, 0, 1]
        heap = [(1 + n - 1, 0, 0, 1)]
        while len(heap) > 0:
            es, row, col, dis = heappop(heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if row == n - 1 and col == n - 1:
                return dis
            else:
                for i in d:
                    for j in d:
                        new_row, new_col = i + row, j + col
                        if (new_row, new_col) in visited or not (0 <= new_row < n and 0 <= new_col < n):
                            continue
                        if grid[new_row][new_col] == 0:
                            heappush(
                                heap, (dis + max(n - new_row - 1, n - new_col - 1), new_row, new_col, dis + 1))
        return -1


test = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
ans = Solution()
ans.shortestPathBinaryMatrix(test)


