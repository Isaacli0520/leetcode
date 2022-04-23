class Solution:
    # Give cells that changes state (from live to dead
    # or dead to live) unique values to record its prev
    # state and its updated state.
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        
        def helper(board, r, c):
            cnt = 0
            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    i, j = r + a, c + b
                    if (a != 0 or b != 0) and i >= 0 and i < row and j >= 0 and j < col:
                        if board[i][j] == 2 or board[i][j] == 1:
                            cnt += 1
            return cnt
        
        for i in range(row):
            for j in range(col):
                lives = helper(board, i, j)
                if board[i][j] and (lives < 2 or lives > 3):
                    board[i][j] = 2
                elif not board[i][j] and lives == 3:
                    board[i][j] = 3
                    
        for i in range(row):
            for j in range(col):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1