class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def preorder_helper(root):
            if root:
                ans.append(root.val)
                if root.left:
                    preorder_helper(root.left)
                if root.right:
                    preorder_helper(root.right)
        preorder_helper(root)
        return ans
