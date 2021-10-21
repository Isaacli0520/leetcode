class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        # Initialize Last Row
        row = [0 for i in range(c)]
        # Initialize bottom-right corner
        row[0] = 1 - obstacleGrid[r - 1][c - 1]
        # DP from finish point to start
        # Indices are r - i - 1 and c - j - 1 instead of i, j
        for i in range(r):
            row[0] = 0 if obstacleGrid[r - i - 1][-1] else row[0]
            for j in range(1, c):
                row[j] = (row[j - 1] + row[j]) if not obstacleGrid[r - i - 1][c - j - 1] else 0
        return row[-1]
                