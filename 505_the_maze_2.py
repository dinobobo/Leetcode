from collections import deque


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        def move(row, col, direction):
            steps = 0
            if direction == 1:
                while col - 1 >= 0 and not maze[row][col - 1]:
                    col -= 1
                    steps += 1
            elif direction == 2:
                while row - 1 >= 0 and not maze[row - 1][col]:
                    row -= 1
                    steps += 1
            elif direction == 3:
                while col + 1 < n and not maze[row][col + 1]:
                    col += 1
                    steps += 1
            else:
                while row + 1 < m and not maze[row + 1][col]:
                    row += 1
                    steps += 1
            return (row, col, steps)

        # move to left, top, right, down
        m, n = len(maze), len(maze[0])
        d = (1, 2, 3, 4)
        visited = {(start[0], start[1]): 0}
        q = deque([[start[0], start[1], 0]])

        while len(q) > 0:
            length = len(q)
            for i in range(length):
                row, col, steps = q.pop()
                for j in d:
                    new_row, new_col, new_steps = move(row, col, j)
                    if new_row == row and new_col == col:
                        continue
                    if (new_row, new_col) not in visited or \
                            ((new_row, new_col) in visited and visited[(new_row, new_col)] > steps + new_steps):
                        q.appendleft([new_row, new_col, steps + new_steps])
                        visited[(new_row, new_col)] = steps + new_steps

        return visited[(destination[0], destination[1])] if (destination[0], destination[1]) in visited else -1


maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]
ans = Solution()
ans.shortestDistance(maze, start, destination)
