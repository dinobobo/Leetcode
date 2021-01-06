# User two pointers to trace even and odd nodes. Be careful how to
# swap the nodes. Remember to assign next FIRST!
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        if not head:
            return head
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow.next, fast.next.next, fast.next = fast.next, slow.next, fast.next.next
            slow = slow.next
            fast = fast.next
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

ans = Solution()
ans.oddEvenList(head)
