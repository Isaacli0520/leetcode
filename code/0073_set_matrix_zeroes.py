class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = len(matrix), len(matrix[0])
        
        # Check if first row and first col have zeroes 
        # The reason is that the first cell cannot encode 
        # info about both first row and first col
        first_row, first_col = False, False
        for i in range(r):
            if matrix[i][0] == 0:
                first_col = True
                break
        
        for j in range(c):
            if matrix[0][j] == 0:
                first_row = True
                break
        
        # Check other rows and cols
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Update
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        if first_row:
            for i in range(c):
                matrix[0][i] = 0
        if first_col:
            for i in range(r):
                matrix[i][0] = 0