class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(idx, track):
            res.append(track)
            for i in range(idx, len(nums)):
                helper(i + 1, track + [nums[i]])
        helper(0, [])
        return res