class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        
        def dfs(m, n):
            if not (m >= 0 and m < r) or not(n >= 0 and n < c) or grid[m][n] != 0:
                return
            grid[m][n] = 1
            for i, j in [(m - 1, n), (m + 1, n), (m, n - 1), (m, n + 1)]:
                dfs(i, j)
        
        # Flood border islands
        for i in [0, r - 1]:
            for j in range(c):
                dfs(i, j)
        for i in range(r):
            for j in [0, c - 1]:
                dfs(i, j)
        
        cnt = 0
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    cnt += 1
        return cnt
        