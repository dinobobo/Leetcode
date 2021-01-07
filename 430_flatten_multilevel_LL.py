class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# Recursive solution
'''
    Make a copy of the cur.next when linking the cur to child.
    Terminate the child.
'''


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head:
            self.flatten_list(head)
        return head

    def flatten_list(self, cur):
        if not cur.next and not cur.child:
            return cur
        old_next = cur.next
        if cur.child:
            cur.next = cur.child
            cur.child.prev = cur
            tail = self.flatten_list(cur.child)
            if old_next:
                tail.next = old_next
                old_next.prev = tail
            cur.child = None
        if old_next:
            tail = self.flatten_list(old_next)
        return tail


# An easier implementation of the recursive approach:
'''
    Use a sentinel head, and write the recursive function as func(prev, cur).
    Call func(cur, cur.child) and func(tail, cur.next) to finish the recursive call
'''


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        sentinel = Node(0, None, None, None)
        sentinel.next = head
        self.flatten_list(sentinel, head)
        head.prev = None
        return head

    def flatten_list(self, prev, cur):
        if cur == None:
            return prev
        prev.next = cur
        cur.prev = prev
        old_next = cur.next
        tail = self.flatten_list(cur, cur.child)
        cur.child = None
        return self.flatten_list(tail, old_next)


# Iterative solution: just like the standard preorder BST traversal
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        sentinel = Node(0, None, None, None)
        sentinel.next = head
        node_st = [head]
        prev = sentinel
        while len(node_st) > 0:
            node = node_st.pop()
            if node.next:
                node_st.append(node.next)
            if node.child:
                node_st.append(node.child)
            node.child = None
            prev.next = node
            node.prev = prev
            prev = node
        head.prev = None
        return head


ans = Solution()
node1 = Node(1, None, None, None)
node2 = Node(2, None, None, None)
node3 = Node(3, None, None, None)
node4 = Node(4, None, None, None)
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node2.child = node4

ans.flatten(node1)
