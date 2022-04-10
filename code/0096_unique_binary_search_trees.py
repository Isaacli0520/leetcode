class Solution:
    # DP Recursive
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        
        def helper(length):
            if dp[length] > 0:
                return dp[length]

            for i in range(length):
                dp[length] += helper(i) * helper(length - i - 1)
            return dp[length]
        
        return helper(n)

    # DP Iterative
    def numTrees(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        # 2 ~ n
        for i in range(2, n + 1):
            # dp(3) = dp(0) * dp(2) + dp(1) * dp(1) + dp(2) * dp(0)
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]