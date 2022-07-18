class Solution:
    # DP
    # dp[i][0 or 1]
    # dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - price[i])
    # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + price[i])
    def maxProfit(self, prices: List[int]) -> int:
        hold, sell1, sell2 = -prices[0], 0, 0
        for i in range(1, len(prices)):
            hold, sell2, sell1 = max(hold, sell2 - prices[i]), sell1, max(sell1, hold + prices[i])
        return sell1