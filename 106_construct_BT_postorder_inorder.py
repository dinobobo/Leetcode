class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive approach, in postorder, the root is always at the end.


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_l, in_r, po_l, po_r):
            if in_l == in_r:
                return None
            root = TreeNode(postorder[po_r - 1])
            root_idx = inorder.index(root.val)
            root.left = helper(in_l, root_idx, po_l, po_l + root_idx - in_l)
            root.right = helper(root_idx + 1, in_r, po_r -
                                (in_r - root_idx), po_r-1)
            return root
        return helper(0, len(inorder), 0, len(postorder))


# Build a hashmap for index.... We can also keep popping from the postorder, since
# it will basically be the root for different levels of recursive calls.
