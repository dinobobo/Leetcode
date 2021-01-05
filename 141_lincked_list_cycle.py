# Initialize the fast and slow pointer to different nodes, 
# also check fast.next in the while loop to make sure that 
# fast node won't accidentally end up on a None.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        fast = head.next
        slow = head
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return False if fast.next == None else True