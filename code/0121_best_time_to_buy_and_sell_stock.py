class Solution:
    # DP
    # dp[i] = maximum profit on day i
    # dp[i] = max(dp[i - 1], prices[i] - min_sofar)
    # min_sofar = min(min_sofar, prices[i])
    def maxProfit(self, prices: List[int]) -> int:
        min_sofar = prices[0]
        maxi = 0
        for i in range(1, len(prices)):
            maxi = max(maxi, prices[i] - min_sofar)
            min_sofar = min(min_sofar, prices[i])
        return maxi
    
    # Find maximum subarray of difference array
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        maxi_curr = 0
        for i in range(1, len(prices)):
            maxi_curr = max(prices[i] - prices[i - 1], maxi_curr + prices[i] - prices[i - 1])
            maxi = max(maxi, maxi_curr)
        return max(maxi, 0)