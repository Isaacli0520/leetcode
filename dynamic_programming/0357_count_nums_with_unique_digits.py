class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        tot = 10
        mul = 9 * 9
        for i in range(n - 1):
            tot += mul
            mul *= (8 - i)
        return tot