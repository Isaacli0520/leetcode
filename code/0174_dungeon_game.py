class Solution:
    # DP optimized
    # For 2d dp array:
    # dp[i][j] = min health required to get to bottom right from (i, j)
    # Then build dp array from bottom right to top left
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r, c = len(dungeon), len(dungeon[0])
        dp = [0 for j in range(c)]
        dp[-1] = 1 if dungeon[-1][-1] >= 0 else 1 - dungeon[-1][-1]
        
        for i in range(c - 2, -1, -1):
            health_needed = dp[i + 1] - dungeon[-1][i]
            dp[i] = health_needed if health_needed > 0 else 1
        
        for i in range(r - 2, -1, -1):
            health_needed = dp[-1] - dungeon[i][-1]
            dp[-1] = health_needed if health_needed > 0 else 1
            for j in range(c - 2, -1, -1):
                mini = min(dp[j], dp[j + 1])
                health_needed = mini - dungeon[i][j]
                dp[j] = health_needed if health_needed > 0 else 1
        
        return dp[0]
    
    # DP
    # dp[i][j] = min health required to get to bottom right from (i, j)
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r, c = len(dungeon), len(dungeon[0])
        dp = [[0 for j in range(c)] for i in range(r)]
        dp[-1][-1] = 1 if dungeon[-1][-1] >= 0 else 1 - dungeon[-1][-1]
        
        for i in range(c - 2, -1, -1):
            health_needed = dp[-1][i + 1] - dungeon[-1][i]
            dp[-1][i] = health_needed if health_needed > 0 else 1
        
        for i in range(r - 2, -1, -1):
            health_needed = dp[i + 1][-1] - dungeon[i][-1]
            dp[i][-1] = health_needed if health_needed > 0 else 1
        
        for i in range(r - 2, -1, -1):
            for j in range(c - 2, -1, -1):
                mini = min(dp[i + 1][j], dp[i][j + 1])
                health_needed = mini - dungeon[i][j]
                dp[i][j] = health_needed if health_needed > 0 else 1
        
        return dp[0][0]
                