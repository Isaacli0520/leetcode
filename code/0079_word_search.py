class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        visited = [[False] * c for _ in range(r)]
        
        def helper(m, n, idx):
            if idx == len(word):
                return True
            if not (m >= 0 and m < r) or not (n >= 0 and n < c) or visited[m][n] or board[m][n] != word[idx]:
                return False
            
            visited[m][n] = True
            for i, j in [(m - 1, n), (m, n - 1), (m + 1, n), (m, n + 1)]:
                if helper(i, j, idx + 1):
                    return True
            visited[m][n] = False
            return False
        
        for i in range(r):
            for j in range(c):
                if helper(i, j, 0):
                    return True
        return False