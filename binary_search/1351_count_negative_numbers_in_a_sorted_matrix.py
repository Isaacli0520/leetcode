class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0
        for i in range(m):
            left = 0
            right = n - 1
            while(left <= right):
                mid = int(left + (right - left) / 2)
                if grid[i][mid] < 0:
                    right = mid - 1
                elif grid[i][mid] >= 0:
                    left = mid + 1
            if (left >= n or grid[i][left] >= 0):
                continue;
            total += (n - left)
        return total
    
    # def countNegatives(self, grid: List[List[int]]) -> int:
    #     m, n = len(grid), len(grid[0])
    #     total, j = 0, 0
    #     for i in range(m - 1, -1, -1):
    #         while(j < n):
    #             if grid[i][j] < 0:
    #                 total += n - j
    #                 break
    #             j += 1
    #     return total
                