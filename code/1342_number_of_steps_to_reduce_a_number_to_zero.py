class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 1 if num == 0 else 0
        while num > 0:
            res += 1 + (num & 1)
            num >>= 1
        return res - 1