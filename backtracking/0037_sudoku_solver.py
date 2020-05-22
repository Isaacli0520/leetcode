class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.nums = ['1','2','3','4','5','6','7','8','9']
        self.solve(board)
        
    def solve(self, board):
        # Find next empty cell
        r, c = -1, -1
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    r, c = i, j
                    break
                    
        # If no empty cell, retruen true
        if r == -1 and c == -1:
            return True
        
        # Fill in with numbers
        # Backtracking
        for num in self.nums:
            if self.isValid(board, r, c, num):
                board[r][c] = num
                if self.solve(board):
                    return True
                board[r][c] = "."
            
    def isValid(self, board, r, c, ch):
        # Row
        for i in range(9):
            if board[r][i] == ch:
                return False
        # Col
        for i in range(9):
            if board[i][c] == ch:
                return False 
            
        # Grid
        s_r, s_c = r - r % 3, c - c % 3
        for i in range(s_r, s_r + 3):
            for j in range(s_c, s_c + 3):
                if board[i][j] == ch:
                    return False
        return True
                