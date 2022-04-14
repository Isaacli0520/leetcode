class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def helper(path, start, diff, cnt):
            if diff == 0 and cnt == k:
                res.append(path[:])
                return
            if cnt >= k:
                return
            for i in range(start, 10):
                if i <= diff:
                    path.append(i)
                    helper(path, i + 1, diff - i, cnt + 1)
                    path.pop()
                    
        helper([], 1, n, 0)
        return res