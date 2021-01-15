from collections import deque


class Solution:
    D = [0, 1, 0, -1, 0]

    def updateMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        ans = [[0] * cols for _ in range(rows)]

        def BFS(row, col):
            stack = deque([[row, col]])
            d = 1
            origin_row = row
            origin_col = col
            while len(stack) > 0:
                length = len(stack)
                for _ in range(length):
                    row, col = stack.pop()
                    for i in range(4):
                        next_row = row + self.D[i]
                        next_col = col + self.D[i + 1]
                        if 0 <= next_row < rows and 0 <= next_col < cols:
                            if matrix[next_row][next_col] == 0:
                                ans[origin_row][origin_col] = d
                                return
                            else:
                                stack.appendleft([next_row, next_col])
                d += 1

            return

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1:
                    BFS(row, col)
        return ans

# Improve use a set to replace the stack. Other visited ones can be stored.

# A single BFS starting from ALL of the 0s!!! See this before.

# Two sweeps using DP.


test = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
solution = Solution()
ans = solution.updateMatrix(test)
print(ans)
