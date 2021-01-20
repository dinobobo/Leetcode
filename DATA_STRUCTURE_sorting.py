# Merge sort
class Solution:
    def sortArray(self, nums):

        def helper(l, r):
            if l + 1 == r:
                return nums[l:r]
            mid = (l + r)//2
            left_arr = helper(l, mid)
            right_arr = helper(mid, r)
            i = 0
            j = 0
            arr = []
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    arr.append(left_arr[i])
                    i += 1
                else:
                    arr.append(right_arr[j])
                    j += 1
            arr += left_arr[i:]
            arr += right_arr[j:]
            return arr
        return helper(0, len(nums))


# Quick sort.
class Quick_sort:
    def quick_sort(self, l, r, arr):
        if r <= l + 1:
            return
        else:
            pivot = self.partition(l, r, arr)
            self.quick_sort(l, pivot, arr)
            self.quick_sort(pivot + 1, r, arr)
        return arr

    def partition(self, l, r, arr):
        slow = l
        fast = l
        piv = arr[r - 1]
        while fast < r:
            if arr[fast] < piv:
                arr[fast], arr[slow] = arr[slow], arr[fast]
                slow += 1
            fast += 1
        arr[r - 1], arr[slow] = arr[slow], arr[r - 1]
        return slow


arr = [5, 4, 11, 0, 3, 7, 10, 4, 1, 6]
q_sort = Quick_sort()
pivot = q_sort.quick_sort(0, len(arr), arr)
print(arr)
