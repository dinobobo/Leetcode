# The key to terminate the sudoku is to not remove the number when the end is reached.
# In this case, all the backtracks will not be valid will all return.
from collections import defaultdict


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def place_number(row, col, number):
            board[row][col] = str(number)
            zone_idx = row // 3 * 3 + col // 3
            zones[zone_idx][number] += 1
            rows[row][number] += 1
            cols[col][number] += 1

        def delete_number(row, col, number):
            board[row][col] = '.'
            zone_idx = row//3*3 + col // 3
            zones[zone_idx].pop(number)
            rows[row].pop(number)
            cols[col].pop(number)

        def is_valid(row, col, number):
            zone_idx = row//3*3 + col // 3
            return number not in rows[row] and \
                number not in cols[col] and \
                number not in zones[zone_idx]

        def helper(row, col):
            if row == N:
                nonlocal over
                over = True
                return
            new_row = row + (col + 1) // N
            new_col = (col + 1) % N
            if board[row][col].isdigit():
                helper(new_row, new_col)
            else:
                for num in range(1, N + 1):
                    if is_valid(row, col, num):
                        place_number(row, col, num)
                        helper(new_row, new_col)
                        if not over:
                            delete_number(row, col, num)

        N = 9
        rows = [defaultdict(int) for _ in range(N)]
        cols = [defaultdict(int) for _ in range(N)]
        # index with row//3*3 + col // 3
        zones = [defaultdict(int) for _ in range(N)]
        for row in range(N):
            for col in range(N):
                num = board[row][col]
                if num.isdigit():
                    place_number(row, col, int(num))
        over = False

        helper(0, 0)


test = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."], [
            "8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"], [
            "7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."], [
        ".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solution = Solution()
ans = solution.solveSudoku(test)
