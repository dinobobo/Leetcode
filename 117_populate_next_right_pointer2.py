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

        def add_nodes(arr, node):
            if len(arr) < 2:
                nodes.append(node)
                if len(arr) == 2:
                    arr[0].next = arr[1]
            else:
                arr.pop(0)
                arr.append(node)
                arr[0].next = arr[1]
        start = root
        while start:
            curr = start
            nodes = []
            start = None
            while curr:
                if curr.left:
                    if not start:
                        start = curr.left
                    add_nodes(nodes, curr.left)
                if curr.right:
                    if not start:
                        start = curr.right
                    add_nodes(nodes, curr.right)
                if curr.next:
                    curr = curr.next
                else:
                    break
        return root


# Use recursive?
