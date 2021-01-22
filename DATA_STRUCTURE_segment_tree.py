# Properties
# 1. Leaf Nodes are the elements of the input array.
# 2. Each internal node represents some merging of the leaf nodes. The merging may be different for different problems.
# For this problem, merging is sum of leaves under a node.
# 3. An array representation of tree is used to represent Segment Trees. For each node at index i, the left child is at index 2*i+1, right child at 2*i+2 and the parent is at
from math import ceil, log2


class SegmentTree():

    def construct_sum_seg(self, arr, n):
        # Allocate memory for the segment tree
        # Height of segment tree
        x = int((ceil(log2(n))))

        # Maximum size of segment tree
        max_size = 2**(x + 1) - 1
        # Allocate memory
        segtree = [0] * max_size
        # Fill the allocated memory st
        self.sum_seg(arr, 0, n, segtree, 0)
        # Return the constructed segment tree
        return segtree

    def construct_min_seg(self, arr, n):
        # Allocate memory for the segment tree
        # Height of segment tree
        x = int((ceil(log2(n))))

        # Maximum size of segment tree
        max_size = 2**(x + 1) - 1
        # Allocate memory
        segtree = [0]*max_size
        # Fill the allocated memory st
        self.min_seg(arr, 0, n, segtree, 0)
        # Return the constructed segment tree
        return segtree

    def construct_min_seg_idx(self, arr, n):
        # Allocate memory for the segment tree
        # Height of segment tree
        x = int((ceil(log2(n))))

        # Maximum size of segment tree
        max_size = 2**(x + 1) - 1
        # Allocate memory
        segtree = [0] * max_size
        # Fill the allocated memory st
        self.min_seg_idx(arr, 0, n, segtree, 0)
        # Return the constructed segment tree
        return segtree

    def sum_seg(self, arr, l, r, segtree, curr):

        # If there is one element in array,
        # store it in current node of
        # segment tree and return
        if (l + 1 == r):
            segtree[curr] = arr[l]
            return arr[l]
        # If there are more than one elements,
        # then recur for left and right subtrees
        # and store the sum of values in this node
        mid = l + (r - l) // 2
        segtree[curr] = self.sum_seg(
            arr, l, mid, segtree, curr * 2 + 1) + self.sum_seg(arr, mid, r, segtree, curr * 2 + 2)
        return segtree[curr]

    def get_sum(self, l, r, arr_l, arr_r, curr, segtree):
        if arr_l >= r or arr_r <= l:
            return 0
        elif arr_l >= l and arr_r <= r:
            return segtree[curr]
        else:
            mid = arr_l + (arr_r - arr_l)//2
            return self.get_sum(l, r, arr_l, mid, curr*2 + 1, segtree) + self.get_sum(l, r, mid, arr_r, curr*2 + 2, segtree)

    def min_seg(self, arr, l, r, segtree, curr):
        if l == r - 1:
            segtree[curr] = arr[l]
            return arr[l]
        else:
            mid = l + (r - l) // 2
            segtree[curr] = min(self.min_seg(
                arr, l, mid, segtree, curr*2 + 1), self.min_seg(arr, mid, r, segtree, curr*2 + 2))
        return segtree[curr]

    def min_seg_idx(self, arr, l, r, segtree, curr):
        if l == r - 1:
            segtree[curr] = l
        else:
            mid = l + (r - l) // 2
            left_idx = self.min_seg_idx(arr, l, mid, segtree, curr*2 + 1)
            right_idx = self.min_seg_idx(arr, mid, r, segtree, curr*2 + 2)
            if arr[left_idx] < arr[right_idx]:
                segtree[curr] = left_idx
            else:
                segtree[curr] = right_idx
        return segtree[curr]

    def get_min(self, l, r, arr_l, arr_r, curr, segtree):
        if arr_l >= r or arr_r <= l:
            return float('inf')
        elif arr_l >= l and arr_r <= r:
            return segtree[curr]
        else:
            mid = arr_l + (arr_r - arr_l)//2
            return min(self.get_min(l, r, arr_l, mid, curr*2 + 1, segtree), self.get_min(l, r, mid, arr_r, curr*2 + 2, segtree))

    def get_min_idx(self, l, r, arr_l, arr_r, curr, segtree, arr):
        if arr_l >= r or arr_r <= l:
            return -1
        elif arr_l >= l and arr_r <= r:
            return segtree[curr]
        else:
            mid = arr_l + (arr_r - arr_l)//2
            left_idx = self.get_min_idx(
                l, r, arr_l, mid, curr*2 + 1, segtree, arr)
            right_idx = self.get_min_idx(
                l, r, mid, arr_r, curr*2 + 2, segtree, arr)
            if right_idx == -1:
                return left_idx
            if left_idx == -1:
                return right_idx
            if arr[right_idx] > arr[left_idx]:
                return left_idx
            else:
                return right_idx

    def max_seg(self, arr, l, r, segtree, curr):
        if l == r - 1:
            segtree[curr] = arr[l]
            return arr[l]
        else:
            mid = l + (r - l) // 2
            segtree[curr] = max(self.max_seg(
                arr, segtree, l, mid, curr*2 + 1), self.max_seg(arr, segtree, mid, r, curr*2 + 2))
        return segtree[curr]


test = [2, 1, 5, 6, 2, 3]
solution = SegmentTree()
segtree = solution.construct_min_seg_idx(test, len(test))
print(solution.get_min_idx(2, 4, 0, len(test), 0, segtree, test))
