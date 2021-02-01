# Binary search, be careful with the left bound.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return num == 1
        else:
            l, r = 1, num//2
            while l <= r:
                mid = l + (r - l)//2
                if mid**2 == num:
                    return True
                elif mid**2 < num:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
