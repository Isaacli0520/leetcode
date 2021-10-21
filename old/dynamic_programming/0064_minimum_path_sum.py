class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        
        # Initialize Last Row
        row = [grid[-1][i] for i in range(c)]
        for i in range(c - 2, -1, -1):
            row[i] += row[i + 1]
            
        # Build the grid from bottom-right
        for i in range(r - 2, -1, -1):
            row[-1] += grid[i][-1]
            for j in range(c - 2, -1, -1):
                row[j] = grid[i][j] + min(row[j + 1], row[j])
                
        return row[0]