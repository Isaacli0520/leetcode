class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(idx, track):
            res.append(track)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                helper(i + 1, track + [nums[i]])
        helper(0, [])
        return res