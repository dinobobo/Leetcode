# Backtracking problems:
# Decision making, constraints (when to stop or whether we should pursue a path?), and goal.


class Solution:
    def totalNQueens(self, n: int):
        def helper(row, visited, count):
            if row == n:
                count += 1
            else:
                for col in range(n):
                    if self.is_open(row, col, visited):
                        self.place_queens(row, col, visited)
                        count = helper(row + 1, visited, count)
                        self.remove_queens(row, col, visited)
            return count
        visited = [set() for _ in range(3)]
        return helper(0, visited, 0)
       


    def place_queens(self, row, col, visited):  # visited is row, col, diag, anti_diag
        visited[0].add(col)
        visited[1].add(row + col)
        visited[2].add(row - col)

    def remove_queens(self, row, col, visited):
        visited[0].remove(col)
        visited[1].remove(row + col)
        visited[2].remove(row - col)

    def is_open(self, row, col, visited):
        if col not in visited[0] and row + col not in visited[1] and row - col not in visited[2]:
            return True
        else:
            return False


# bit manipulation


solution = Solution()
ans = solution.totalNQueens(40)
