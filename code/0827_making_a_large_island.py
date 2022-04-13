class Solution:
    # DFS
    # DFS every cell, color them with a number, and save a number to area dict
    # Go through cells of 0 and check its maximum area with its connected islands
    def largestIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        areas = {}
        cnt = 2
        maxi = 0
        
        def dfs(i, j):
            if not (i >= 0 and i < r) or not (j >= 0 and j < c) or grid[i][j] != 1:
                return 0
            grid[i][j] = cnt
            area = 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            return area
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    areas[cnt] = dfs(i, j)
                    maxi = max(maxi, areas[cnt])
                    cnt += 1
                    
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    area = 1
                    curr = set()
                    for m, n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if (m >= 0 and m < r) and (n >= 0 and n < c) and grid[m][n] > 1 and grid[m][n] not in curr:
                            curr.add(grid[m][n])
                            area += areas[grid[m][n]]
                    maxi = max(maxi, area)
        return maxi