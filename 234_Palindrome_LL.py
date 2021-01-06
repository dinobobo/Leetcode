# Find the total number of nodes, reverse the second half and compare with
# the first half.
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        node_num = 0
        node_it = head
        while node_it != None:
            node_num += 1
            node_it = node_it.next
        mid_num = node_num // 2
        cur = head
        for _ in range(mid_num):
            cur = cur.next
        prev, cur = cur, cur.next
        while cur != None:
            prev, cur.next, cur = cur, prev, cur.next
        tail = prev
        while mid_num != 0:
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next
            mid_num -= 1
        return True
