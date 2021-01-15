# Using stack, careful with a repeat with multiple digits
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                sub_str = ''
                char_temp = stack.pop()
                while char_temp != '[':
                    sub_str = char_temp + sub_str
                    char_temp = stack.pop()
                repeat = ''
                while stack and stack[-1].isdigit():
                    digit = stack.pop()
                    repeat = digit + repeat
                if digit.isalpha():
                    stack.append(digit)
                stack.append(sub_str * int(repeat))
            else:
                stack.append(char)
        return ''.join(stack)


# Use two stacks. Push strings in the bracket into the stack.
# When there is an opening bracket, the string and k have to be
# pushed into the stack to betracked
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        inner_str = ''
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char is '[':
                stack.append(inner_str)
                stack.append(num)
                inner_str = ""
                num = 0
            elif char is ']':
                repeat = stack.pop()
                outer_str = stack.pop()
                inner_str = outer_str + inner_str*repeat
            else:
                inner_str += char
        return inner_str

# Recursive approach. Kinda obvious since we are working on brackets in brackets.


class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i):
            num = 0
            outer_str = ''
            while i < len(s):
                while s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                while s[i].isalpha():
                    outer_str += s[i]
                    i += 1
                if s[i] == '[':
                    i, inner_str = helper(i + 1)
                    outer_str = outer_str + num * inner_str
                    num = 0
                else :
                    return i + 1, outer_str            
            return outer_str
        return helper(0)
