class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l <= 1:
            return 0
        # Get Differences
        diff = []
        for i in range(1, l):
            diff.append(prices[i] - prices[i - 1])
        # Get subarray with maximum sum
        for i in range(1, l - 1):
            diff[i] += diff[i - 1] if diff[i - 1] > 0 else 0
        m = max(diff)
        return m if m > 0 else 0