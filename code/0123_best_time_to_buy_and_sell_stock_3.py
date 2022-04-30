class Solution:
    # DP
    # dp[i][k][0 or 1] = day i, can complete at most k transactions, hold
    #                    a stock or not
    #
    # dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - price[i])
    # Since k stands for at day i, you can complete at most k transactions,
    # dp[i - 1][k - 1][0] makes sure that before day i - 1, you can complete
    # at most k - 1 transactions, since on day i you are gonna buy a stock
    #
    # dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + price[i]) 
    def maxProfit(self, prices: List[int]) -> int:
        
        prev_2_1, prev_2_0, prev_1_1, prev_1_0 = -prices[0], 0, -prices[0], 0
        for i in range(1, len(prices)):
            prev_2_0 = max(prev_2_0, prev_2_1 + prices[i])
            prev_2_1 = max(prev_2_1, prev_1_0 - prices[i])
            prev_1_0 = max(prev_1_0, prev_1_1 + prices[i])
            prev_1_1 = max(prev_1_1, -prices[i])
            # dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - price[i])
            # dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + price[i]) 
        return prev_2_0