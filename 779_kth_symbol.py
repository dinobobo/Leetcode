class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        if K % 2 != 0:
            return self.kthGrammar(N - 1, (K + 1)//2)
        else:
            return 1 - self.kthGrammar(N - 1, (K + 1)//2)
