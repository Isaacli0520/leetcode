class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def helper(path, start, length):
            if length == k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                helper(path, i + 1, length + 1)
                path.pop()
        
        helper([], 1, 0)
        return res