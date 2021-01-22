from typing import List


# Back tracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = list(map(chr, range(97, 97 + 26)))
        num2let = {}
        for i in range(2, 7):
            num2let[str(i)] = letters[(i - 2) * 3: (i - 1)*3]
        num2let[str(7)] = letters[15:19]
        num2let[str(8)] = letters[19:22]
        num2let[str(9)] = letters[22:26]

        def back_track(num, sub_ans):
            if num == len(digits):
                ans.append(''.join(sub_ans[:]))
            else:
                lets = num2let[digits[num]]
                for let in lets:
                    sub_ans.append(let)
                    back_track(num + 1, sub_ans)
                    sub_ans.pop()

        ans = []
        back_track(0, [])
        return ans

# BFS should work too.
