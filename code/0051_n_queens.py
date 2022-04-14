class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        def isValid(path, pos):
            # Check top
            if pos in path:
                return False
            # Check top-left and top-right
            for i in range(len(path)):
                if path[len(path) - 1 - i] == pos - i - 1 or path[len(path) - 1 - i] == pos + i + 1:
                    return False
            return True
            
        def helper(path):
            if len(path) == n:
                res.append(["." * path[i] + "Q" + "." * (n - path[i] - 1) for i in range(n)])
                return
            for i in range(n):
                if isValid(path, i):
                    path.append(i)
                    helper(path)
                    path.pop()
        helper([])
        return res