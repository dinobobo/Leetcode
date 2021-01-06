# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# In place solution


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel1 = ListNode(0)
        sentinel1.next = l1
        sentinel2 = ListNode(0)
        sentinel2.next = l2
        cur1 = sentinel1
        cur2 = sentinel2
        while cur1.next != None and cur2.next != None:
            if cur1.next.val > cur2.next.val:
                new_node = ListNode(cur2.next.val)
                new_node.next = cur1.next
                cur1.next, cur1, cur2 = new_node, new_node, cur2.next
            else:
                cur1 = cur1.next
        if cur1.next == None:
            while cur2.next != None:
                new_node = ListNode(cur2.next.val)
                new_node.next = cur1.next
                cur1.next, cur1, cur2 = new_node, new_node, cur2.next
        return sentinel1.next


# An easier approach, add a sentinel node on l1. Using two pointers on l1 and l2 and also cur
# to track the position for the updated array. Try and see implementation in the discussion.
# Recursive and iterative?


l1 = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(2)
solution = Solution()
solution.mergeTwoLists(l1, l2)
