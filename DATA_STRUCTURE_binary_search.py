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


# Different templates:

# Most basic and elementary form of Binary Search
# Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it)
# No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

# An advanced way to implement Binary Search.
# Search Condition needs to access element's immediate right neighbor
# Use element's right neighbor to determine if condition is met and decide whether to go left or right
# Gurantees Search Space is at least 2 in size at each step
# Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.


def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1


# An alternative way to implement Binary Search
# Search Condition needs to access element's immediate left and right neighbors
# Use element's neighbors to determine if condition is met and decide whether to go left or right
# Gurantees Search Space is at least 3 in size at each step
# Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1
