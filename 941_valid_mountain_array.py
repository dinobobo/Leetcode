# Go up find the peak and check if it straight decends.
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 1
        while i < len(arr) and arr[i] > arr[i - 1]:
            i += 1
        if i == len(arr) or i == 1:
            return False
        else:
            while i < len(arr):
                if arr[i] >= arr[i - 1]:
                    return False
                i += 1
        return True
