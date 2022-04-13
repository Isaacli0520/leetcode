class Solution:
    # DFS O(n) Visit each island once
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        
        def dfs(i, j):
            if not(i >= 0 and i < r) or not(j >= 0 and j < c) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        
        maxi = 0
        for i in range(r):
            for j in range(c):
                maxi = max(maxi, dfs(i, j))
        return maxi
    
    # Union Find
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        uf = [[(i, j) for j in range(c)] for i in range(r)]
        sizes  = [[grid[i][j] for j in range(c)] for i in range(r)]
        
        def find(x):
            if x != uf[x[0]][x[1]]:
                uf[x[0]][x[1]] = find(uf[x[0]][x[1]])
            return uf[x[0]][x[1]]
        
        def connect(a, b):
            ax, ay, bx, by = *find(a), *find(b)
            if ax == bx and ay == by:
                return
            if sizes[ax][ay] > sizes[bx][by]:
                uf[bx][by] = (ax, ay)
                sizes[ax][ay] += sizes[bx][by]
            else:
                uf[ax][ay] = (bx, by)
                sizes[bx][by] += sizes[ax][ay]
                
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    for m, n in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                        if (m >= 0 and m < r) and (n >= 0 and n < c) and grid[m][n]:
                            connect((i, j), (m, n))             
        return max([max(row) for row in sizes])