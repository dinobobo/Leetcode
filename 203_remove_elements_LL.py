# Add a sentinel node
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        senti_node = ListNode(0)
        senti_node.next = head
        prev = senti_node
        cur = head
        while cur != None:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return senti_node.next