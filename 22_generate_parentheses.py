from typing import List

# Backtracking


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        brackets = {'(': n, ')': n}

        def back_track(count, sub_ans, bra_excess):
            if count == n*2:
                ans.append(''.join(sub_ans[:]))
            if brackets['('] > 0:
                brackets['('] -= 1
                sub_ans.append('(')
                back_track(count + 1, sub_ans, bra_excess + 1)
                sub_ans.pop(-1)
                brackets['('] += 1

            if brackets[')'] > 0 and bra_excess > 0:
                brackets[')'] -= 1
                sub_ans.append(')')
                back_track(count + 1, sub_ans, bra_excess - 1)
                sub_ans.pop(-1)
                brackets[')'] += 1

        ans = []
        back_track(0, [], 0)
        return ans

# Closure number
# fn = (f0)fn-1 + (f1)fn-2 + .....
# The reason being the closure number (minimum index that makes the string a valid
# parenthesis set) defines a unique solution. We can see that the closure number for
# each combination in fn = .... is different.


class Solution(object):
    def generateParenthesis(self, N):
        if N == 0:
            return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans


solution = Solution()
ans = solution.generateParenthesis(2)
