class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    count += 1
        return count
                
    def dfs(self, i, j, board):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "1":
            return
        board[i][j] = "#"
        for m, n in [(i, j - 1),(i - 1, j),(i + 1,j),(i,j + 1)]:
            self.dfs(m, n, board)
        