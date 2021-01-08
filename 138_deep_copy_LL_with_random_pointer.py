class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# Fisrt make a copy node following the original node, so that in the second pass when we are looking for random,
# it always follows the old node.


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = head
        while cur != None:
            copy = Node(cur.val)
            cur.next, cur, copy.next = copy, cur.next, cur.next
        senti_node = Node(0)
        cur = senti_node
        old = head
        new = head.next
        while old != None:
            if old.random != None:
                new.random = old.random.next
            else:
                new.random = None
            cur.next, cur = new, new
            if new.next != None:
                old, new = new.next, new.next.next
            else:
                old = None
        return senti_node.next


# Recursive approach, careful with where to use the old node and where
# to use the new node.
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        visited = {}

        def copy_helper(curr):
            if curr == None:
                return None
            if curr in visited:
                return visited[curr]
            new_node = Node(curr.val)
            visited[curr] = new_node
            new_node.next = copy_helper(curr.next)
            new_node.random = copy_helper(curr.random)
            return new_node
        return copy_helper(head)

# Simple iterative, track the visited ones. We don't have to create a new node
# if the current node we are visiting has been visited.


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        visited = {}
        curr = head
        while curr != None:
            # proceed
            if curr not in visited:
                new_curr = Node(curr.val)
                visited[curr] = new_curr
            else:
                new_curr = visited[curr]
            if curr.random:
                if curr.random not in visited:
                    new_rand = Node(curr.random.val)
                else:
                    new_rand = visited[curr.random]
                visited[curr.random] = new_rand
                new_curr.random = new_rand
            if curr.next:
                if curr.next not in visited:
                    new_next = Node(curr.next.val)
                else:
                    new_next = visited[curr.next]
                visited[curr.next] = new_next
                new_curr.next = new_next
            curr = curr.next
        return visited[head]
