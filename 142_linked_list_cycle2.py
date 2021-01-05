# Start from the same head and use fast and slow to traverse the list
# Note, we need to advance before check fast == slow to make sure head
# won't terminate the loop. This is another way to implement the cycle 
# detection (code wise) compare to 141. Now if we find the first coincide
# node and put another pointer to the head, when they meet again, it's
# the intersection. Some simple math can explain it.... Consider X steps to
# intersect and the cycle has Y edges. Derive from there.

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        def is_cycle(head):
            fast = head
            slow = head
            while fast != None and fast.next != None:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return slow
            return None
        
        coincide_node = is_cycle(head)
        if not coincide_node:
            return None
        start_node = head
        while start_node != coincide_node:
            start_node = start_node.next
            coincide_node = coincide_node.next
        return start_node