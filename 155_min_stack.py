# Use a second stack!
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.min_stack.append([x, 1])
        else:
            if x < self.getMin():
                self.min_stack.append([x, 1])
            elif x == self.getMin():
                self.min_stack[-1][1] += 1
        self.stack.append(x)

    def pop(self) -> None:
        num = self.stack.pop()
        curr_min = self.getMin()
        if curr_min < num:
            pass
        elif curr_min == num:
            if self.min_stack[-1][1] == 1:
                self.min_stack.pop()
            else:
                self.min_stack[-1][1] -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]
