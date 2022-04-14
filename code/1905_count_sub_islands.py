class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        r, c = len(grid1), len(grid1[0])
        
        def dfs(grid, m, n):
            if not(0 <= m and m < r) or not(0 <= n and n < c) or grid[m][n] != 1:
                return
            grid[m][n] = 0
            for i, j in [(m - 1, n), (m + 1, n), (m, n - 1), (m, n + 1)]:
                dfs(grid, i, j)
        
        # Sink islands in grid2 that are water in grid1
        for i in range(r):
            for j in range(c):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(grid2, i, j)
        
        # The rest are all sub-islands
        cnt = 0
        for i in range(r):
            for j in range(c):
                if grid2[i][j] == 1:
                    dfs(grid2, i, j)
                    cnt += 1
        return cnt
                    
                    