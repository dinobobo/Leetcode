# Simple operations on LL. Need to know how negative values or out of bound values handling.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = Node(0)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.size - 1 or index < 0:
            return -1
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            index = 0
        if index <= self.size:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            insert_node = Node(val)
            insert_node.next = cur.next
            cur.next = insert_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= 0 and index < self.size:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            cur.next = cur.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Double linked list implementation
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None


# class MyLinkedList:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.size = 0
#         self.head = Node(0)


#     def get(self, index: int) -> int:
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         if index > self.size - 1 or index < 0:
#             return -1
#         cur = self.head
#         for _ in range(index + 1):
#             cur = cur.next
#         return cur.val


#     def addAtHead(self, val: int) -> None:
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         self.addAtIndex(0, val)


#     def addAtTail(self, val: int) -> None:
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         self.addAtIndex(self.size, val)


#     def addAtIndex(self, index: int, val: int) -> None:
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         if index < 0:
#             index = 0
#         if index <= self.size:
#             cur = self.head
#             for _ in range(index):
#                 cur = cur.next
#             insert_node = Node(val)
#             insert_node.next = cur.next
#             insert_node.prev = cur
#             if cur.next != None:
#                 cur.next.prev = insert_node
#             cur.next = insert_node
#             self.size += 1


#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         if index >= 0 and index < self.size:
#             cur = self.head
#             for _ in range(index):
#                 cur = cur.next
#             if cur.next.next != None:
#                 cur.next.next.prev = cur
#             cur.next = cur.next.next
#             self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
