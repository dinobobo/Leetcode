from typing import List
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cans = [[i[0], i[1]] for i in Counter(candidates).items()]
        n = len(cans)
        ans = []

        def back_tracking(idx, curr_sum, arr):
            val, freq = cans[idx]
            curr_sum += val
            arr += [val]
            if curr_sum == target:
                ans.append(arr)
                return
            elif curr_sum > target:
                return
            else:
                if freq > 1:
                    cans[idx][1] -= 1
                    for j in range(idx, n):
                        back_tracking(j, curr_sum, arr[::])
                    cans[idx][1] += 1
                else:
                    for i in range(idx + 1, n):
                        back_tracking(i, curr_sum, arr[::])

        for i, j in enumerate(cans):
            back_tracking(i, 0, [])
        return ans


test = [1, 2, 7, 6, 1, 5]
target = 8
ans = Solution()
ans.combinationSum2(test, target)
