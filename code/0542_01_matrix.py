class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        res = [[-1] * c for i in range(r)]
        q = deque([])
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    q.append((i, j))
                    res[i][j] = 0
        
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for m, n in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= m < r and 0 <= n < c and res[m][n] == -1:
                        res[m][n] = 1 + res[x][y]
                        q.append((m, n))
        return res
                        
                        