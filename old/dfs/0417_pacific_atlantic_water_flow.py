class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        r, c = len(matrix), len(matrix[0])
        visited = [[0 for j in range(c)] for i in range(r)]
        
        def dfs(i, j):
            for m, n in [(i - 1, j),(i, j - 1),(i + 1, j),(i, j + 1)]:
                if 0 <= m < r and 0 <= n < c and not visited[m][n] and matrix[m][n] >= matrix[i][j]:
                    visited[m][n] = 1
                    dfs(m, n)
        # Init atlantic and pacific with borders
        pacific = [(i, 0) for i in range(r)] + [(0, i) for i in range(c)]
        atlantic = [(i, c - 1) for i in range(r)] + [(r - 1, i) for i in range(c)]
        # Dfs pacific
        for i, j in pacific:
            dfs(i, j)
        pacific += [(i, j) for i in range(r) for j in range(c) if visited[i][j]]
        
        # Dfs atlantic
        visited = [[0 for j in range(c)] for i in range(r)]    
        for i, j in atlantic:
            dfs(i, j)
        atlantic += [(i, j) for i in range(r) for j in range(c) if visited[i][j]]
        
        # Intersection of atlantic and pacific
        return set.intersection(set(atlantic), set(pacific))
        
                        
                