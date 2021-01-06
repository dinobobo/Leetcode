# Iterative. Move the cur.next to the head, and keep track this head as
# the previous head, so that it can be linked in the next iteration.
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        prev_head = head
        while cur != None and cur.next != None:
            head = cur.next
            cur.next = cur.next.next
            head.next, prev_head = prev_head, head
        return head

# Recursive, get the tail of the already completed recursion and link the current node
# to the tail
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse_sublist(head):
            if head.next == None:
                return [head, head]
            next_head, next_tail = reverse_sublist(head.next)
            head.next = None
            next_tail.next = head
            return next_head, head
        if head == None:
            return None
        return reverse_sublist(head)[0]


# Another easier way to do it without return the tail:
# Assume n(k + 1)... is reversed, then we only have to link
# nk.next.next = nk, and make nk.next = None
