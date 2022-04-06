class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reflect (Reverse left to right)
        for i in range(r):
            for j in range(c // 2):
                matrix[i][j], matrix[i][c - j - 1] = matrix[i][c - j - 1], matrix[i][j]
        