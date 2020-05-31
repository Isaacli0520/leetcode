class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        visited = [[0 for j in range(c)] for i in range(r)]
        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or not grid[i][j] or visited[i][j]:
                return 0
            visited[i][j] = 1
            return 1 + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i + 1, j) + dfs(i, j + 1)
        ret = 0
        for i in range(r):
            for j in range(c):
                if not visited[i][j] and grid[i][j]:
                    ret = max(ret, dfs(i, j))
        return ret