class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        r, c = len(matrix), len(matrix[0])
        left, right = 0, r*c - 1
        while(left <= right):
            mid = int(right + (left - right) / 2)
            val = matrix[mid // c][mid % c]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
        return False