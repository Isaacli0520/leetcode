class Solution:
    # DP Optimized
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(amount + 1):
                if coin <= j:
                    dp[j] = dp[j] + dp[j - coin]
        return dp[-1]
    
    # DP
    # dp[i][j] = number of ways to use coins[:i] to make up j
    #        Use coin[i - 1]: dp[i][j] = dp[i][j - coins[i - 1]]
    # Do not use coin[i - 1]: dp[i][j] = dp[i - 1][j]
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
                