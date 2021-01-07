class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# Insert either in the body or by the end. Careful with the situation that all the nodes
# have the same value.


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        elif not head.next:
            head.next = Node(insertVal)
            head.next.next = head
            return head
        else:
            prev = head
            cur = head.next
            while cur != head:
                if cur.val >= insertVal and prev.val <= insertVal:
                    prev.next = Node(insertVal)
                    prev.next.next = cur
                    return head
                elif cur.val < prev.val and (insertVal >= prev.val or insertVal <= cur.val):
                    prev.next = Node(insertVal)
                    prev.next.next = cur
                    return head
                else:
                    prev, cur = cur, cur.next
            prev.next = Node(insertVal)
            prev.next.next = cur
            return head


# Simplify using the next parameter to insert the node.
# Insertd of repeating the insertion code, we can check if insertion is necessary
# and then do the insert
