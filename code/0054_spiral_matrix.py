class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        tot = len(matrix) * len(matrix[0])
        top = 0
        right = len(matrix[0]) - 1
        left = 0
        bot = len(matrix) - 1
        res = []
        while len(res) < tot:
            # Top
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
                
            # Right
            for i in range(top, bot + 1):
                res.append(matrix[i][right])
            right -= 1
                
            # Bottom
            if top <= bot:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bot][i])
                bot -= 1
                
            # Left
            if left <= right:
                for i in range(bot, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
            