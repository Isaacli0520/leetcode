class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(r, c, s, idx):
            if idx == len(s):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != s[idx]:
                return False
            # Mark board[r][c] as visited
            tmp = board[r][c]
            board[r][c] = "#"
            # Visit neighbors
            for a, b in [(r - 1,c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if helper(a, b, s, idx + 1):
                    return True
            # Restore
            board[r][c] = tmp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, word, 0):
                    return True
        return False