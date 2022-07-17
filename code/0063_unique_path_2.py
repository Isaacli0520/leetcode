class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * c
        dp[0] = 1 - obstacleGrid[0][0]
        
        for i in range(r):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, c):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] = dp[j - 1] + dp[j]
        return dp[-1]