
# Backtracking
class Solution:
    def __init__(self):
        self.dic_p = {}
        self.dic_s = {}
        self.ans = False

    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        # bijective mapping, has to be exclusive both ways.

        def backtrack(kp, ks):
            if kp == m:
                if ks == n:
                    self.ans = True
                return
            if pattern[kp] in self.dic_p:
                val = self.dic_p[pattern[kp]]
                if len(val) > n - ks:
                    return
                else:
                    if val == s[ks: ks + len(val)]:
                        backtrack(kp + 1, ks + len(val))
                    else:
                        return
            else:
                for i in range(ks + 1, n + 1):
                    self.dic_p[pattern[kp]] = s[ks: i]
                    if s[ks: i] in self.dic_s:
                        self.dic_p.pop(pattern[kp])
                        continue
                    else:
                        self.dic_s[s[ks: i]] = pattern[kp]
                        backtrack(kp + 1, i)
                        if self.ans == True:
                            return
                        self.dic_p.pop(pattern[kp])
                        self.dic_s.pop(s[ks: i])

        m, n = len(pattern), len(s)
        backtrack(0, 0)
        return self.ans


ans = Solution()
ans.wordPatternMatch('a', 'b')
