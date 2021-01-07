class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# Fisrt make a copy node following the original node, so that in the second pass when we are looking for random,
# it always follows the old node.


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = head
        while cur != None:
            copy = Node(cur.val)
            cur.next, cur, copy.next = copy, cur.next, cur.next
        senti_node = Node(0)
        cur = senti_node
        old = head
        new = head.next
        while old != None:
            if old.random != None:
                new.random = old.random.next
            else:
                new.random = None
            cur.next, cur = new, new
            if new.next != None:
                old, new = new.next, new.next.next
            else:
                old = None
        return senti_node.next
