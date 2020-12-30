'''
This problem is actually a bit tricky. The idea is to do it in place and neglect the elements that
are pushed out of the array by duplicating zeros.
1. Count the zeros. Note, if the last element is 0 (index + number of previous zeros + 1 == length),
 this 0 can not be duplicated. Instead, we copy
 this 0 to the end and reduce the arr length that we should modify by 1
2. Use two pointer to point to the copy location and traversal location. Copy.
'''


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        zero_nums = 0
        for i, num in enumerate(arr):
            if (zero_nums + i + 1) > length:
                break
            elif num == 0:
                if zero_nums + i + 1 == length:
                    length -= 1
                    arr[-1] = 0
                else:
                    zero_nums += 1
        trav_i = length - zero_nums - 1
        copy_i = length - 1
        while trav_i >= 0:
            if arr[trav_i] == 0:
                arr[copy_i] = 0
                arr[copy_i - 1] = 0
                trav_i -= 1
                copy_i -= 2
            else:
                arr[copy_i] = arr[trav_i]
                trav_i -= 1
                copy_i -= 1
        return None
