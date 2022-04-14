class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.nums = [str(i) for i in range(1, 10)]
        self.solve(board)
    
    def findEmptyCell(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    return i, j
        return -1, -1
    
    def solve(self, board):
        r, c = self.findEmptyCell(board)
        
        if r == -1 and c == -1:
            return True
        
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