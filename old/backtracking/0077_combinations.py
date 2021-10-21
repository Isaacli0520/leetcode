class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(nums, idx, track):
            if len(track) == k:
                res.append(track)
            for i in range(idx, n):
                helper(nums, i + 1, track + [nums[i]])
        helper(list(range(1, n + 1)), 0, [])
        return res