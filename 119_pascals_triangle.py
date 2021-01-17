# Recursive
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        ans = [1] * (rowIndex + 1)
        prev = self.getRow(rowIndex - 1)
        for i in range(len(prev) - 1):
            ans[i + 1] = prev[i] + prev[i + 1]
        return ans
