class Solution:
    # Iterative
    # Example: x ^ 9
    # 9 = 1001 in binary
    # x^9 = x^(2^3) * x^(2^0)
    # multiply result with 2^i at bits that are 1s
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            n = -n
            x = 1 / x
        while n:
            if n % 2 == 1:
                res *= x
            x *= x
            n = n // 2
        return res
    
    # Recursive
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = abs(n)
        
        num = self.myPow(x, n // 2)
        if n % 2 == 1:
            return num * num * x
        else:
            return num * num