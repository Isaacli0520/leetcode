class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = 0
        right = n - 1
        bot = n - 1
        left = 0
        
        res = [[0] * n for i in range(n)]
        cnt = 1
        while left <= right and top <= bot:
            # Top
            for i in range(left, right + 1):
                res[top][i] = cnt
                cnt += 1
            top += 1
            
            # Right
            for i in range(top, bot + 1):
                res[i][right] = cnt
                cnt += 1
            right -= 1
            
            # Bottom
            if top <= bot:
                for i in range(right, left - 1, -1):
                    res[bot][i] = cnt
                    cnt += 1
                bot -= 1
            
            # Left
            if left <= right:
                for i in range(bot, top - 1, -1):
                    res[i][left] = cnt
                    cnt += 1
                left += 1
            
        return res