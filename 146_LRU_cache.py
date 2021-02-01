# from collections import OrderedDict

# # The built in data structure


# class LRUCache(OrderedDict):

#     def __init__(self, capacity: int):
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         else:
#             self.move_to_end(key)
#             return self[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self[key] = value
#             self.move_to_end(key)
#         else:
#             if len(self) + 1 > self.capacity:
#                 self.popitem(last=False)
#             self[key] = value


# Doubly linked list
# Use Doubly linked list in addition to a dictionary
# Dictionary: key : node
# node: prev, next, val, key
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def add_node(self, node):
        self.head.next.prev, self.head.next, node.prev, node.next = node, node, self.head, self.head.next

    def move_to_end(self, node):
        # remove from original position
        node.prev.next, node.next.prev = node.next, node.prev
        # add behind the head
        self.add_node(node)

    def remove_left(self):
        key = self.tail.prev.key
        self.cache.pop(key)
        self.tail.prev.prev.next, self.tail.prev = self.tail, self.tail.prev.prev

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.move_to_end(node)
            return self.cache[key].val

    def put(self, key, val):
        if key in self.cache:
            # update the node
            node = self.cache[key]
            node.val = val
            # move to the end
            self.move_to_end(node)
        else:
            node = Node(key, val)
            if len(self.cache) + 1 > self.capacity:

                # remove both the node and the item in the dictionary
                self.remove_left()
            # add node and dict
            self.add_node(node)
            self.cache[key] = node


test = LRUCache(2)
test.put(1, 1)
test.put(2, 2)
test.get(1)
test.put(3, 3)
test.get(2)
test.put(4, 4)
test.get(1)
test.get(3)
test.get(4)
