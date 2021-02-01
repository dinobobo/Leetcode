from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            while l <= r:
                mid = l + (r - l)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        l, r = 0, len(nums) - 1
        while r >= l:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    return binary_search(l, mid - 1)
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    return binary_search(mid + 1, r)
                else:
                    r = mid - 1
        return -1


ans = Solution()
test = [3, 1]
target = 1
ans.search(test, target)
