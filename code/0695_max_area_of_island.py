class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        
        def dfs(i, j):
            grid[i][j] = 0
            area = 1
            for (m, n) in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                if 0 <= m < r and 0 <= n < c and grid[m][n]:
                    area += dfs(m, n)
            return area
         
        max_area = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    max_area = max(max_area, dfs(i, j))
        return max_area