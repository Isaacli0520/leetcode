class Solution:
    # DP
    # dp[i][0 or 1]
    # dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - price[i])
    # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + price[i])
    def maxProfit(self, prices: List[int]) -> int:
        prev1_0, curr1, curr0 = 0, -prices[0], 0
        for price in prices:
            prev2_0 = prev1_0
            prev1_0 = curr0
            curr0 = max(curr0, curr1 + price)
            curr1 = max(curr1, prev2_0 - price)
        return curr0