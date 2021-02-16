from typing import List


# class Solution:
#     def letterCasePermutation(self, S: str) -> List[str]:
#         ans = [[]]
#         for c in S:
#             if c.isalpha():
#                 ans += [i[::] for i in ans]
#                 for i in range(len(ans) // 2):
#                     ans[i].append(c.upper())
#                 for j in range(len(ans)//2, len(ans)):
#                     ans[j].append(c.lower())
#             else:
#                 for k in ans:
#                     k.append(c)
#         print(ans)
#         return [''.join(i) for i in ans]

# bit_mask
class Solution(object):
    def letterCasePermutation(self, S):
        B = sum(letter.isalpha() for letter in S)
        ans = []

        for bits in range(1 << B):
            b = 0
            word = []
            for letter in S:
                if letter.isalpha():
                    # This is examine the binary form ######, from right to left, if each digit is 1.
                    if (bits >> b) & 1:
                        word.append(letter.lower())
                    else:
                        word.append(letter.upper())

                    b += 1
                else:
                    word.append(letter)

            ans.append("".join(word))
        return ans


test = "a1b2"
ans = Solution()
ans.letterCasePermutation(test)
