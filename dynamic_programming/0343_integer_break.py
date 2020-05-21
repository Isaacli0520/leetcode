class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1 for i in range(n + 1)]
        dp[1] = 1
        for i in range(1, n + 1):
            for j in range(1, i):
                # Q: Why the inner max?
                # A: Because dp[2] = 1 < 2, dp[5] = 6 > 5
                dp[i] = max(dp[i], max(dp[i - j], i - j) * j)
        return dp[-1]