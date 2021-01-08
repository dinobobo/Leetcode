class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def postorder_helper(root):
            if root:
                if root.left:
                    postorder_helper(root.left)
                if root.right:
                    postorder_helper(root.right)
                ans.append(root.val)
        postorder_helper(root)
        return ans
