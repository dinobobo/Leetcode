from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(node1, node2):
    if not node1 and not node2:
        return True
    elif not node1 or not node2:
        return False
    else:
        return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)


# Use a deque and BFS. For loop is not necessary


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        dq = deque([root.left, root.right])
        while len(dq) > 0:
            dq_len = len(dq)
            for _ in range(dq_len//2):
                node_l = dq.pop()
                node_r = dq.pop()
                if node_l:
                    if node_r:
                        if node_l.val == node_r.val:
                            dq.appendleft(node_l.left)
                            dq.appendleft(node_r.right)
                            dq.appendleft(node_l.right)
                            dq.appendleft(node_r.left)
                        else:
                            return False
                    else:
                        return False
                else:
                    if node_r:
                        return False
                    else:
                        pass
        return True
