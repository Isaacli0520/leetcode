class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def helper(t, idx, track):
            if len(track) == k and t == 0:
                res.append(track)
                return
            for i in range(idx, min(t + 1, 10)):
                helper(t - i, i + 1, track + [i])
        helper(n, 1, [])
        return res