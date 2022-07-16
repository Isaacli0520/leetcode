class Solution:
    # DP
    # dp[i, j] = minimum sum of path ended at point (i, j)
    # dp[i, j] = grid[i, j] + min(dp[i - 1][j], dp[i][j - 1])
    # Since we build dp from top left, row by row, from left to right,
    # we only need one row instead of a 2d array to store the dp table
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [grid[0][0]]
        for i in range(1, c):
            dp.append(dp[-1] + grid[0][i])
        for i in range(1, r):
            dp[0] += grid[i][0]
            for j in range(1, c):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]