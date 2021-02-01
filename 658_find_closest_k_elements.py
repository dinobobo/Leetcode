class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def binary_search(l, r):
            while l <= r:
                mid = l + (r - l)//2
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    r = mid - 1
                else:
                    l = mid + 1
            return r
        mid = binary_search(0, len(arr) - 1)

        i, j = mid, mid + 1
        k_temp = k
        while i >= 0 and j < len(arr) and k_temp > 0:
            if abs(arr[j] - x) < abs(x - arr[i]):
                j += 1
            else:
                i -= 1
            k_temp -= 1

        if i < 0:
            return arr[: k]
        elif j == len(arr):
            return arr[len(arr) - k:len(arr)]
        else:
            return arr[i + 1: j]


# Change the logic so that i and j will increment or decrement when the limit is hit?
