class Solution:
    # DP
    # dp[i][j] = maximum coins you can collect by bursting balloons from i + 1 to j - 1 (therefore not including i, j)
    #   dp[i][k]   dp[k][j]
    #    -------     ----
    # i  |     |  k  |  |  j
    # 1, 2, 3, 4, 5, 6, 7, 8
    # dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j], dp[i][j])
    # Since dp[i][j] depends on smaller j and bigger i, we have to go from
    # right to left for i, and left to right for j and k
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j], dp[i][j])
        return dp[0][-1]