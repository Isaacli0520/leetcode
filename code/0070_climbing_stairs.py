class Solution:
    def climbStairs(self, n: int) -> int:
        dp1, dp2 = 1, 1
        for i in range(n):
            dp1, dp2 = dp2, dp1 + dp2
        return dp1