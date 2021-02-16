from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def move(row, col, direction):
            if direction == 1:
                while col - 1 >= 0 and not maze[row][col - 1]:
                    col -= 1
            elif direction == 2:
                while row - 1 >= 0 and not maze[row - 1][col]:
                    row -= 1
            elif direction == 3:
                while col + 1 < n and not maze[row][col + 1]:
                    col += 1
            else:
                while row + 1 < m and not maze[row + 1][col]:
                    row += 1
            return (row, col)

        def search_maze(row, col):
            if [row, col] == destination:
                return True

            if (row, col) in visited:
                return False
            else:
                visited.add((row, col))

            for direction in d:
                new_row, new_col = move(row, col, direction)
                if new_row == row and new_col == col:
                    continue
                if search_maze(new_row, new_col):
                    return True
            return False

        # move to left, top, right, down
        m, n = len(maze), len(maze[0])
        d = (1, 2, 3, 4)
        visited = set()
        return search_maze(start[0], start[1])
