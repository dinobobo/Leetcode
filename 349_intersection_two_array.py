class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(l, r, target):
            while l <= r:
                mid = l + (r - l)//2
                if nums2[mid] == target:
                    return mid
                elif nums2[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        def helper(l1, r1, l2, r2, ans):
            if l1 > r1 or l2 > r2:
                return
            mid1 = l1 + (r1 - l1)//2
            mid2 = binary_search(l2, r2, nums1[mid1])
            if mid2 == r2 + 1:
                helper(l1, mid1 - 1, l2, mid2 - 1, ans)
                return
            if nums1[mid1] == nums2[mid2]:
                ans.add(nums1[mid1])
            helper(l1, mid1 - 1, l2, mid2 - 1, ans)
            helper(mid1 + 1, r1, mid2, r2, ans)

        nums1.sort()
        nums2.sort()
        ans = set([])
        helper(0, len(nums1) - 1, 0, len(nums2) - 1, ans)
        return ans

# Use two pointer after sorting. The above method is silly since the time complexity is  O(NlogN) after the sorting
