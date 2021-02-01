# Find boundary and binary search
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # Binary search
        def binary_search(l, r):
            while l <= r:
                mid = l + (r - l)//2
                if reader.get(mid) == target:
                    return mid
                elif reader.get(mid) > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        # Find boundary
        l, r = 0, 1
        while reader.get(r) < target and reader.get(r) != 2147483647:
            l = r
            r *= 2
        return binary_search(l, r)
