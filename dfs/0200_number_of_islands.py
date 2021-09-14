class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        r, c = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != "1":
                return
            grid[i][j] = "#"
            for m, n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                dfs(m, n)
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
    