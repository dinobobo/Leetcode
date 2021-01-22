class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = []
        stack.append((p, q))
        while len(stack) != 0:
            p, q = stack.pop()
            if bool(p) != bool(q):
                return False
            elif p and q:
                if p.val != q.val:
                    return False
                else:
                    stack.append((p.left, q.left))
                    stack.append((p.right, q.right))
        return True
