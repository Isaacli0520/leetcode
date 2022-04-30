class Solution:
    # DP
    # dp[i][0 or 1]
    # dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
    # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp0, dp1 = 0, -prices[0] - fee
        for i in range(1, len(prices)):
            dp0, dp1 = max(dp0, dp1 + prices[i]), max(dp1, dp0 - prices[i] - fee)
        return dp0