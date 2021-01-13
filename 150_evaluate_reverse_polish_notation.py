class Solution:
    def evalRPN(self, tokens) -> int:
        operators = {'+', '-', '/', '*'}
        nums = []
        for token in tokens:
            if token not in operators:
                nums.append(token)
            else:
                num2 = nums.pop()
                num1 = nums.pop()
                ans = str(int(eval(num1 + token + num2)))
                nums.append(ans)
        return nums[-1]

# In place with two pointers?


test = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
solution = Solution()
ans = solution.evalRPN(test)
