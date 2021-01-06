# Keep a slow pointer that tails the fast one by n 
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

# Try introduce a sentinel node and make the fast node advance by n + 1?