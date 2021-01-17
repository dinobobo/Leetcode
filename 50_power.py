class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 2:
            return x**n
        else:
            half = self.myPow(x, n//2)
            return half ** 2 if n % 2 == 0 else x*half**2
