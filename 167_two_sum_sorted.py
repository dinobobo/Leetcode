from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while j >= i:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                mid = i + (j - i) // 2
                while numbers[i] + numbers[mid] > target:
                    j = mid
                    mid = i + (j - i) // 2
                j -= 1
            else:
                mid = i + (j - i) // 2
                while numbers[j] + numbers[mid] < target:
                    i = mid
                    mid = i + (j - i) // 2
                i += 1


test = [5, 25, 75]
target = 100
ans = Solution()
ans.twoSum(test, target)
