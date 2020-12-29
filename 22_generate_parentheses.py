class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def add_paren(left, right, s):
            if right == n:
                ans.append(s)
                return
            if left > right:
                add_paren(left, right + 1, s + ')')
            if left < n:
                add_paren(left + 1, right, s + '(')
        add_paren(0, 0, '')
        return ans
