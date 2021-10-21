class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0 for i in range(num + 1)]
        dp[0] = 0
        for i in range(1, num + 1):
            # If even, amount[i] = amount[i / 2] because last bit is 0
            # If odd, amount[i] = amount[i - 1] + 1 because last bit is 1
            if i % 2 == 0:
                dp[i] = dp[i >> 1]
            else:
                dp[i] = dp[i - 1] + 1
        return dp