class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        visited = [[False] * c for _ in range(r)]
        
        def dfs(m, n):
            if not (m >= 0 and m < r) or not(n >= 0 and n < c) or visited[m][n] or grid[m][n] != "1":
                return
            visited[m][n] = True
            for i, j in [(m - 1, n), (m + 1, n), (m, n - 1), (m, n + 1)]:
                dfs(i, j)
        
        cnt = 0
        for i in range(r):
            for j in range(c):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        return cnt