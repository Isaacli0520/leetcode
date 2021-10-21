class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1. Check all boundary and related cells that are "O"
        #    and change them to "#"
        # 2. Change "#" to "O" and all other cells to "X"
        
        if not board:
            return
        r, c = len(board), len(board[0])
        # Push all boundaries to stack
        stack = []
        for i in range(r):
            stack += [(i, 0), (i, c - 1)]
        for i in range(c):
            stack += [(0, i), (r - 1, i)]
            
        # Check all boundary and related cells that are "O"
        # Change them to "#"
        while stack:
            i, j = stack.pop()
            if 0 <= i < r and 0 <= j < c and board[i][j] == "O":
                board[i][j] = "#"
                stack += [(i, j - 1),(i - 1, j),(i + 1,j),(i,j + 1)]
                
        # Change every cell but "#" cells to "X"
        for i in range(r):
            for j in range(c):
                board[i][j] = "O" if board[i][j] == "#" else "X"
                