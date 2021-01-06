# Once one LL is at the end, switch the node to the head of the other, and eventually
# the two pointers are going to meet at the intersect if there is one.
# Gotta consider the case of say, one is head == None, and also when they both reach
# to the None when there is no intersection.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        curA = headA
        curB = headB
        while curA != curB:
            if curA.next == None and curB.next == None:
                return None
            if curA.next == None:
                curA = headB
            else:
                curA = curA.next
            if curB.next == None:
                curB = headA
            else:
                curB = curB.next
        return curA