class Solution:
    # DP
    # dp[i][1 or 0] = on day i, you may hold a stock or not
    #                 and this represents the maximum profit
    #
    # dp[i][1] = max(dp[i - 1][0] - price[i], dp[i - 1][1])
    # the maximum profit on day i when you hold a stock is the maximum of
    #   1. You hold a stock on day i - 1 and continue holding it
    #   2. You buy a stock on day i while you have no stock on day i - 1
    #
    # dp[i][0] = max(dp[i - 1][1] + price[i], dp[i - 1][0])
    # Similaryly,
    #   1. You sell the stock that you hold on day i - 1
    #   2. You continue to have no stock as on day i - 1
    def maxProfit(self, prices: List[int]) -> int:
        prev_1, prev_0 = -prices[0], 0
        for i in range(1, len(prices)):
            prev_1, prev_0 = max(prev_0 - prices[i], prev_1), max(prev_1 + prices[i], prev_0)
        return prev_0
    
    # Greedy
    #    -           *4
    #   - -     *2  - -
    #  -   -   - - -   -
    #       - -   *3    -
    #        *1
    # *4 - *1 < *2 - *1 + *4 - *3
    # So always buy and sell when price[i] > price[i - 1]
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
        