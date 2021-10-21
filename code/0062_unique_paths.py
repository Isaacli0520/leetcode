class Solution:
    # Naive DP
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        # Base Cases
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
            
        # Bottom-up
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        return dp[m - 1][n - 1]
    
    # Two rows
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1 for i in range(n)]
        curr = [1 for i in range(n)]
        for i in range(m - 1):
            for j in range(1, n):
                curr[j] = prev[j] + curr[j - 1]
            prev, curr = curr, prev
        return prev[-1]
    
    # One Row
    def uniquePaths(self, m: int, n: int) -> int:
        curr = [1 for i in range(n)]
        for i in range(m - 1):
            for j in range(1, n):
                curr[j] += curr[j - 1]
        return curr[-1]