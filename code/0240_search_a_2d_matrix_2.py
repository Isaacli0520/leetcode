class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        j = len(matrix[0]) - 1
        if j == -1:
            return False
        for row in matrix:
            while j > 0 and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False