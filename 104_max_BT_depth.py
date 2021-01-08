class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def depth_helper(node):
            if not node:
                return 0
            return max(depth_helper(node.left), depth_helper(node.right)) + 1

        return depth_helper(root)

# Use a top down approach! depth_helper(node, current_depth) so that we can do a tail recursion
