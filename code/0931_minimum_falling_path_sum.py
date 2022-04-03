class Solution:
    # DP
    # dp[i, j] = minimum sum of path ended at point (i, j)
    # dp[i, j] = dp[i - 1, j - 1] + dp[i - 1, j] + dp[i - 1, j + 1]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for j in range(n)] for i in range(n)]
        dp[0] = matrix[0]
        for r in range(1, n):
            for c in range(n):
                tmp = [dp[r - 1][c]]
                if c > 0:
                    tmp.append(dp[r - 1][c - 1])
                if c < n - 1:
                    tmp.append(dp[r - 1][c + 1])
                dp[r][c] = min(tmp) + matrix[r][c]
        return min(dp[-1])