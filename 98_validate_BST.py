class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, node_min, node_max):
            if not node:
                return True
            if node.val >= node_max or node.val <= node_min:
                return False
            return helper(node.left, node_min, node.val) and helper(node.right, node.val, node_max)
        return helper(root, -float('inf'), float('inf'))

# Compute inorder traversal and check the sorting.
