class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Careful with the 0 rotate case.


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        curr = head
        num = 1
        while curr.next != None:
            num += 1
            curr = curr.next
        tail = curr
        k = k % num
        if k == 0:
            return head
        steps = num - k - 1
        curr = head
        for _ in range(steps):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail.next = head
        return new_head

# Make the list a ring and break.
