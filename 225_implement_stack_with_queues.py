from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque([])
        self.q2 = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """

        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.empty():
            return self.q1.popleft()
        else:
            return None

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.empty():
            return self.q1[0]
        else:
            return None

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0


# It can be O(1) is in the push operation, we can just attach the entire deque, since this only takes a node link.
