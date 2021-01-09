class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# There are three conditions to observe, node.val is p or q, left tree has p or q, and
# right tree has p or q. If two of them are satisfied, node will be the common ancestor.


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if node == p or node == q:
                mid = 1
            else:
                mid = 0

            if node.left:
                left = helper(node.left)
            else:
                left = 0

            if node.right:
                right = helper(node.right)
            else:
                right = 0
            if left + right + mid == 2:
                self.ans = node
            return mid or left or right
        helper(root)
        return self.ans


# Iterative method. Use a dictionary to track the parent of each node. After we found p and q, track the first
# common parent.



