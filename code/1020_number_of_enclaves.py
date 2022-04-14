class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        
        def dfs(m, n):
            if not(0 <= m and m < r) or not(0 <= n and n < c) or grid[m][n] != 1:
                return 0
            grid[m][n] = 0
            area = 1
            for i, j in [(m - 1, n), (m + 1, n), (m, n - 1), (m, n + 1)]:
                area += dfs(i, j)
            return area
        
        
        for i in [0, r - 1]:
            for j in range(c):
                dfs(i, j)
        
        for j in [0, c - 1]:
            for i in range(r):
                dfs(i, j)
                
        tot = 0
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                if grid[i][j] == 1:
                    tot += dfs(i, j)
        
        return tot