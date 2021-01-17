# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(node):
            if node and node.next:
                follow = node.next.next
                node, node.next = node.next, ListNode(node.val)
                if follow and follow.next:
                    node.next.next = helper(follow)
                else:
                    node.next.next = follow
            return node
        return helper(head)
