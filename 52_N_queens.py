# Return the check board.
class Solution:
    def solveNQueens(self, n: int):
        ans = []

        def helper(row, visited, sub_ans):
            if row == n:
                ans.append(sub_ans.copy())
            else:
                for col in range(n):
                    if self.is_open(row, col, visited):
                        self.place_queens(row, col, visited)
                        sub_ans.append('.'*col + 'Q' + '.' * (n - col - 1))
                        helper(row + 1, visited, sub_ans)
                        self.remove_queens(row, col, visited)
                        sub_ans.pop(-1)
            return
        visited = [set() for _ in range(3)]
        helper(0, visited, [])
        return ans

    def place_queens(self, row, col, visited):  # visited is col, diag, anti_diag
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


solution = Solution()
ans = solution.solveNQueens(4)
