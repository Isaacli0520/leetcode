class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def helper(path, k, n, end):
            if k == 0:
                if n == 0:
                    res.append(path[:])
                return
            
            for i in range(end, 0, -1):
                if n >= i:
                    path.append(i)
                    helper(path, k - 1, n - i, i - 1)
                    path.pop()
            
        helper([], k, n, 9)
        return res