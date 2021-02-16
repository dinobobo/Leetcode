class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node):
            if not node:
                return None
            if node.val < low:
                return trim(node.right)
            elif node.val > high:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        return trim(root)


test = TreeNode(1)
test.left = TreeNode(0)
test.right = TreeNode(2)
low, high = 1, 2
