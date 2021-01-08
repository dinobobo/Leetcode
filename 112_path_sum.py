# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        def helper(node, sub_sum):
            if not node.left and not node.right:
                return node.val == sub_sum
            if node.left:
                is_left = helper(node.left, sub_sum - node.val)
            else:
                is_left = False
            if node.right:
                is_right = helper(node.right, sub_sum - node.val)
            else:
                is_right = False
            return is_left or is_right
        return helper(root, sum)


# Try iterative? 
