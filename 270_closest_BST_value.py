# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        min_dif = float('inf')
        ans = root.val
        node = root
        while node != None:
            if node.val == target:
                return node.val
            elif node.val > target:
                if abs(node.val - target) < min_dif:
                    min_dif = abs(node.val - target)
                    ans = node.val
                node = node.left
            else:
                if abs(node.val - target) < min_dif:
                    min_dif = abs(node.val - target)
                    ans = node.val
                node = node.right
        return ans
