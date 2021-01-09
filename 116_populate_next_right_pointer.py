class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        start = root
        while start.left != None:
            curr = start
            curr.left.next = curr.right
            while curr.next:
                curr.right.next = curr.next.left
                curr = curr.next
                curr.left.next = curr.right
            start = start.left
        return root
