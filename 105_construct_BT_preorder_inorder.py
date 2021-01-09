class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.preorder_idx = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_map = {}
        for i, node_val in enumerate(inorder):
            inorder_map[node_val] = i

        def helper(left, right):
            if left == right:
                return None
            node = TreeNode(preorder[self.preorder_idx])
            self.preorder_idx += 1
            node_idx = inorder_map[node.val]
            node.left = helper(left, node_idx)
            node.right = helper(node_idx + 1, right)
            return node
        return helper(0, len(preorder))
