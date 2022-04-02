class Solution:
    # SubProblem dp[i] = min(dp[i - coin] + 1, dp[i])
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return -1 if dp[amount] == amount + 1 else dp[amount]