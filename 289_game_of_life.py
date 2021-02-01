class Solution:
    d1 = [0, 1, 0, -1, 0]
    d2 = [1, 1, -1, -1, 1]

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # live -> die = 2
        # die -> live = -1
        def get_neighbors(row, col):
            live = 0
            dead = 0
            for i in range(4):
                if 0 <= row + self.d1[i] < rows and 0 <= col + self.d1[i + 1] < cols and \
                        board[row + self.d1[i]][col + self.d1[i + 1]] > 0:
                    live += 1
                if 0 <= row + self.d2[i] < rows and 0 <= col + self.d2[i + 1] < cols and \
                        board[row + self.d2[i]][col + self.d2[i + 1]] > 0:
                    live += 1
            return live
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                live = get_neighbors(row, col)
                if board[row][col] and (live < 2 or live > 3):
                    board[row][col] = 2
                if not board[row][col] and live == 3:
                    board[row][col] = -1
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 2:
                    board[row][col] = 0
                elif board[row][col] == -1:
                    board[row][col] = 1
        return board

# For the infinite case, find the coordinates of the live cells and update.
