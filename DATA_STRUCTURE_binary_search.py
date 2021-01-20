# This binary search always shifts things to the right, i.e. if a number is not
# in the array, it returns the index of the number that's larger than the
# searched number num[i - 1] < val < num[i]. The if val is out of bounds, it returns
# 0 and len(num)


def binary_search(l, r, num, val):
    if l == r:
        return l
    mid = (l + r)//2
    if num[mid] == val:
        return mid
    elif num[mid] > val:
        return binary_search(l, mid, num, val)
    else:
        return binary_search(mid + 1, r, num, val)


num = [1, 2, 3, 4, 5, 6]
val = 5.5
ans = binary_search(0, len(num), num, val)
print(ans)
