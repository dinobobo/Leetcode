# Careful with the edge case of the binary search, since if the search
# result is the length of the array, it causes index out of bounds.
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        def helper(l, r, t, b):
            if t == b or l == r:
                return False
            row = (t + b)//2
            col = self.binary_search(row, l, r, target, matrix)
            if col != r and matrix[row][col] == target:
                return True
            else:
                is_top_right = helper(col, r, t, row)
                is_bot_left = helper(l, col, row + 1, b)
                return is_top_right or is_bot_left
        return helper(0, len(matrix[0]), 0, len(matrix))

    def binary_search(self, row, l, r, val, matrix):
        if l == r:
            return l
        mid = (l + r)//2
        if matrix[row][mid] == val:
            return mid
        elif matrix[row][mid] > val:
            return self.binary_search(row, l, mid, val, matrix)
        else:
            return self.binary_search(row, mid + 1, r, val, matrix)

# Get linear time moving from top-right corner or bottom-left corner.


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
    3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 20
solution = Solution()
ans = solution.searchMatrix(matrix, target)
