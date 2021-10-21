class Solution:
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
            return 0 - res
        else:
            return res