# Backtracking
# from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(start, sub_arr, count):
            if count == k:
                ans.append(sub_arr[:])
            else:
                for num in range(start, n + 1):
                    sub_arr.append(num)
                    helper(num + 1, sub_arr, count + 1)
                    sub_arr.pop(-1)

        helper(1, [], 0)
        return ans


# Iterative?
