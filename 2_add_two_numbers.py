# In place solution. Be careful of how ten is handled, especially when
# one LL is exhausted. Maybe a slightly more consise way is that assume
# the LL that ends early has value 0 and use one while loop to finish.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = ListNode(0)
        prev.next = l1
        cur1 = l1
        cur2 = l2
        tens = 0
        while cur1 != None and cur2 != None:
            tens, rem = divmod(cur1.val + cur2.val + tens, 10)
            cur1.val = rem
            cur1 = cur1.next
            prev = prev.next
            cur2 = cur2.next
        if cur1 == None:
            while cur2 != None:
                tens, rem = divmod(cur2.val + tens, 10)
                prev.next = ListNode(rem)
                prev = prev.next
                cur2 = cur2.next
        else:
            while cur1 != None:
                tens, rem = divmod(cur1.val + tens, 10)
                cur1.val = rem
                cur1 = cur1.next
                prev = prev.next
        if tens == 1:
            prev.next = ListNode(1)
        return l1
