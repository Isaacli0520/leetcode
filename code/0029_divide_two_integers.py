class Solution:
    # 58 / 5 = 11(10) = 1011(2)
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        neg = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        shift, res = 0, 0
        
        while(dividend >= divisor):
            divisor = divisor << 1
            shift += 1
            
        while(shift >= 0):
            if dividend >= divisor:
                res += 1 << shift
                dividend -= divisor
            divisor = divisor >> 1
            shift -= 1
            
        if neg:
            return -res
        else:
            return res

    # 58 / 5 = 11(10) = 1011(2)
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1):
            return 2147483647
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        for i in range(31, -1, -1):
            if (a >> i) - b >= 0:
                res += 1 << i
                a -= b << i
        
        if (dividend > 0) == (divisor > 0):
            return res
        else:
            return -res