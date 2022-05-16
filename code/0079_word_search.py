class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        visited = [[False] * c for _ in range(r)]
        
        def dfs(i, j, k):
            if not(i >= 0 and i < r and j >= 0 and j < c) or visited[i][j]:
                return False
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited[i][j] = True
            for m, n in [(i, j - 1), (i - 1, j), (i + 1, j), (i, j + 1)]:  
                if dfs(m, n, k + 1):
                    return True
            visited[i][j] = False
            return False
        
        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0):
                    return True
        return False
        