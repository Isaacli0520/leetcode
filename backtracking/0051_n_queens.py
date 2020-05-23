class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def solve(board, r):
            if r >= n:
                res.append(["".join(l) for l in board])
                return
            # Row by row Backtracking
            for i in range(n):
                if isValid(board, r, i):
                    board[r][i] = "Q"
                    solve(board, r + 1)
                    board[r][i] = "."
            
        def isValid(board, r, c):
            # Check column
            for i in range(r - 1, -1, -1):
                if board[i][c] == "Q":
                    return False
                
            # Check Top Right
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i, j = i - 1, j + 1
            
            # Check Top Left
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i, j = i - 1, j - 1
            
            return True
        
        solve([["." for j in range(n)] for i in range(n)], 0)
        return res