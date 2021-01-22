class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            if node.left:
                min_left, max_left = helper(node.left)
                node.left = max_left
                max_left.right = node
            else:
                min_left = node
                max_left = node

            if node.right:
                min_right, max_right = helper(node.right)
                node.right = min_right
                min_right.left = node
            else:
                min_right = node
                max_right = node
            return min_left, max_right

        if not root:
            return root
        min_node, max_node = helper(root)
        min_node.left = max_node
        max_node.right = min_node
        return min_node

#  A simple inorder traversal?


class Solution:
    def __init__(self):
        self.prev = None
        self.first = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def helper(node):
            if node:
                helper(node.left)
                if self.first == None:
                    self.first = node
                if self.prev:
                    self.prev.right = node
                    node.left = self.prev
                self.prev = node
                helper(node.right)
        if not root:
            return root
        helper(root)
        self.first.left = self.prev
        self.prev.right = self.first
        return self.first
