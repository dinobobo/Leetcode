from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        dq = deque([])
        dq.append(root)
        while len(dq) > 0:
            st_len = len(dq)
            ans.append([])
            for _ in range(st_len):
                node = dq.pop()
                ans[-1].append(node.val)
                if node.left:
                    dq.appendleft(node.left)
                if node.right:
                    dq.appendleft(node.right)
        return ans
