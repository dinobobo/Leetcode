# Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# queries = [input().split() for _ in range(n)]


#  operations of the following  types:

# 1. append - Append string  to the end of .
# 2. delete - Delete the last  characters of .
# 3. print - Print the  character of .
# 4. undo - Undo the last (not previously undone) operation of type  or , reverting  to the state it was in prior to that operation.


# Use a stack to track the undos. Print is not included in the undo
class TextEditor:
    def __init__(self):
        self.s = ""
        self.deleted = []
        self.undo_stack = []

    def append(self, s, undo=False):
        if not undo:
            self.s += s
        else:
            self.s = self.s[: len(self.s) - len(s)]

    def delete(self, k, undo=False, undo_s=""):
        if undo:
            self.s += undo_s
        else:
            if len(self.s) - k >= 0:
                self.deleted.append(self.s[len(self.s) - k:])
                self.s = self.s[0: len(self.s) - k]
            else:
                self.s = ""
                self.deleted.append(self.s)

    def _print(self, i):
        if 0 <= i - 1 < len(self.s):
            print(self.s[i - 1])

    def execute(self, q, undo, undo_s=''):
        if q[0] == '1':
            self.append(q[1], undo)
        elif q[0] == '2':
            self.delete(int(q[1]), undo, undo_s=undo_s)
        elif q[0] == '3':
            self._print(int(q[1]))

    def parse_q(self, queries):
        dos = '123'
        for i, q in enumerate(queries):
            if q[0] in dos:
                self.execute(q, False)
                if q[0] != '3':
                    self.undo_stack.append(q)
            else:
                if len(self.undo_stack) >= 0:
                    uq = self.undo_stack.pop()
                    if uq[0] == '1':
                        self.execute(uq, True)
                    elif uq[0] == '2':
                        self.execute(uq, True, self.deleted.pop())
            # print(self.s)


queries = [['1', 'abc'], ['3', '3'], ['2', '3'], [
    '1', 'xy'], ['3', '2'], ['4'], ['4'], ['3', '1']]
ans = TextEditor()
ans.parse_q(queries)
