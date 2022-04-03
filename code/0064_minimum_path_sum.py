class Solution:
    # DP
    # dp[i, j] = minimum sum of path ended at point (i, j)
    # dp[i, j] = grid[i, j] + min(dp[i - 1][j], dp[i][j - 1])
    # Since we build dp from top left, row by row, from left to right,
    # we only need one row instead of a 2d array to store the dp table
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [grid[0][c] for c in range(col)]
        for c in range(1, col):
            dp[c] += dp[c - 1]
        
        for r in range(1, row):
            dp[0] += grid[r][0]
            for c in range(1, col):
                dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
        
        return dp[-1]