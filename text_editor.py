# TextEditor实现以下功能：append, backspace, undo, redo, select, bold. input长这样：String[][] input
# append: 在当前字符串结尾append或将选中的字符串replace e.g. ["1", "APPEND", "hello"]
# backspace: 删掉当前字符串最后一位或选中的字符串 e.g. ["2", "BACKSPACE"]
# undo: 撤销上一步操作 e.g. ["3", "UNDO"]-baidu 1point3acres
# redo: 把上一步被撤销的操作重做 e.g. ["4", "REDO"]
# select: 选中当前字符串的某一部分, 给定了[start, end)  e.g. ["5", "SELECT", 3, 6]
# bold: 将选中的字符串bold e.g. ["6", "BOLD"]

# 题目要注意的点和corner case:
# 0. 操作顺序应该按照linux timestamp排序，也就是每个array的第一个element。
# 1. backspace 如果已经没有字符串可以删了，这就是一个无效操作, ignore即可。
# 2. undo 如果已经没有操作可以撤销了，就是一个无效操作, ignore。
# 3. redo 如果已经没有操作可以重做了(#redo > #undo)，ignore。注意redo只能接在undo/redo后面。
# 4. select 如果操作的end超过了当前字符串的末尾，就选到末尾。如果有连续多个select，只有最后一个有效。如果start出界了，整个操作ignore。

# 我想到的但题目没有clarify清楚的：
# 1. select start >= end？我当做ignore处理了
# 2. bold 前面没有select? 当做ignore处理了
# 这样处理完最后所有test case都跑过了

# 实现undo/redo的思路是，用一个stack存所有被undo的operation，后面遇到redo就从栈中取出。注意每遇到非undo/redo操作的时候要清空栈。

# Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# queries = [input().split() for _ in range(n)]


class TextEditor:
    def __init__(self, instructions):
        self.s = ''
        self.sel = None
        self.undos = []
        self.redos = []
        self.instructions = instructions

    def append(self, ins):  # e.g. ["1", "APPEND", "hello"]
        order, _, s = ins
        if self.sel:
            # [instruction, replaced_string, prev_selection]
            self.undos.append(
                [int(order) - 1, self.s[self.sel[0], self.s[1]], self.sel])
            self.s = self.s[:self.sel[0]] + s + self.s[self.sel[1]:]
            self.sel = None
        else:
            self.undos.append([int(order) - 1, '', self.sel])
            self.s += s

    def backspace(self, ins):  # e.g. ["2", "BACKSPACE"]
        order, _ = ins
        if self.sel:
            self.undos.append(
                [int(order) - 1, self.s[self.sel[0]: self.sel[1]], self.sel])
            self.s = self.s[: self.sel[0]] + self.s[self.sel[1]:]
            self.sel = None
        else:
            if len(self.s) > 0:
                self.undos.append([int(order) - 1, self.s[-1], self.sel])
                self.s = self.s[: len(self.s) - 1]
            else:
                pass

    def selector(self, ins):  # e.g. ["5", "SELECT", 3, 6]
        order, _, l, r = ins
        if l >= r:
            pass
        else:
            if r > len(self.s):
                r = len(self.s)
            self.undos.append([int(order) - 1, self.sel])
            self.sel = [l, r]

    def bold(self, ins):  # e.g. ["6", "BOLD"]
        order, _ = ins
        if self.sel:
            self.undos.append([int(order) - 1, self.sel])
            self.s = self.s[: self.sel[0]] + self.s[self.sel[0]
                : self.sel[1]].upper() + self.s[self.sel[1]:]
        else:
            pass

    def edits(self, ins, redo=False):
        if ins[1] not in ['UNDO', 'REDO']:  # not undo/redo
            if ins[1] == 'APPEND':
                self.append(ins)
            elif ins[1] == 'BACKSPACE':
                self.backspace(ins)
            elif ins[1] == 'SELECT':
                self.selector(ins)
            else:
                self.bold(ins)
            if not redo:
                self.redos = []  # Empties redos:
        else:
            if ins[1] == 'UNDO':  # undos
                if len(self.undos) == 0:
                    pass
                else:
                    # update string and bring the selector back
                    undo_ins = self.undos.pop()
                    old_ins = self.instructions[undo_ins[0]]
                    self.redos.append(old_ins)
                    if old_ins[1] == 'APPEND':
                        replaced_s, prev_sel = undo_ins[1:]
                        if prev_sel:
                            self.s = self.s[: prev_sel[0]] + replaced_s + \
                                self.s[prev_sel[0] + len(old_ins[2]):]
                        else:
                            self.s = self.s[: len(
                                self.s) - len(old_ins[2])]
                    elif old_ins[1] == 'BACKSPACE':
                        deleted_s, prev_sel = undo_ins[1:]
                        if prev_sel:
                            self.s = self.s[: prev_sel[0]] + \
                                deleted_s + self.s[prev_sel[0]:]
                        else:
                            self.s += deleted_s
                    elif old_ins[1] == 'SELECT':
                        prev_sel = undo_ins[1]
                    else:
                        prev_sel = undo_ins[1]
                        if prev_sel:
                            self.s = self.s[:prev_sel[0]] + self.s[prev_sel[0]
                                : prev_sel[1]].lower() + self.s[prev_sel[1]:]
                        else:
                            pass
                    self.sel = prev_sel
            else:
                if len(self.redos) > 0:
                    ins = self.redos.pop()
                    self.edits(ins, True)


test = [['1', 'APPEND', 'a'], ['2', 'APPEND', 'a'],
        ['3', 'APPEND', 'a'], ['4', 'UNDO'], ['5', 'UNDO'], ['6', 'UNDO'], ['7', 'UNDO'], ['8', 'REDO'], [
            '9', 'REDO'], ['10', 'REDO'], ['11', 'REDO'], ['12', 'SELECT', 1, 20], ['13', 'BOLD'],
        ['14', 'UNDO'], ['15', 'REDO'], ['16', 'BACKSPACE']]
edit = TextEditor(test)
i = 0
for ins in edit.instructions:
    edit.edits(ins)
    i += 1
    print(i)
    print(edit.s)
