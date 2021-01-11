# Design a circular queue. A bunch of things to consider while deque and enque.
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.head = -1
        self.tail = -1
        self.q = [0]*k

    def enQueue(self, value: int) -> bool:
        # this can be simplified! Cause when there is only one element, you can
        # basically reset the indices and that's it!
        if self.isFull():
            return False
        else:
            self.q[(self.tail + 1) % self.size] = value
            self.tail = (self.tail + 1) % self.size
            if self.head == -1:
                self.head += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q[self.head] = 0
            self.head = (self.head + 1) % self.size
            if self.head == (self.tail + 1) % self.size:
                self.head = -1
                self.tail = -1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[self.tail]

    def isEmpty(self) -> bool:
        return True if self.head == -1 else False

    def isFull(self) -> bool:
        return (self.tail + 1) % self.size == self.head


# A different implementation with head, count, and capacity? Check solution.

# Use linked list?
