class Solution:
    # DP optimized
    def maxProfit(self, K: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp = [[0, -prices[0]] for k in range(K + 1)]
        dp[0][1] = 0
            
        for i in range(1, len(prices)):
            for k in range(1, K + 1):
                dp[k][0] = max(dp[k][0], dp[k][1] + prices[i])
                dp[k][1] = max(dp[k][1], dp[k - 1][0] - prices[i])
        return dp[-1][0]
    
    # DP
    # dp[i][k][0 or 1] = day i, can complete at most k transactions, hold
    #                    a stock or not
    #
    # dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
    # Since k stands for at day i, you can complete at most k transactions,
    # dp[i - 1][k - 1][0] makes sure that before day i - 1, you can complete
    # at most k - 1 transactions, since on day i you are gonna buy a stock
    #
    # dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i]) 
    def maxProfit(self, K: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp = [[[0, 0] for k in range(K + 1)] for i in range(len(prices))]
        for k in range(1, K + 1):
            dp[0][k][1] = -prices[0]
            
        for i in range(1, len(prices)):
            for k in range(1, K + 1):
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
        return dp[-1][-1][0]