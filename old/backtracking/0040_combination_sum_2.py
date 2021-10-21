class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(nums, idx, t, track):
            if t == 0:
                res.append(track)
                return
            for i in range(idx, len(nums)):
                num = nums[i]
                # Skip negative numbers and duplicates
                if t < num or (i > idx and nums[i] == nums[i - 1]):
                    continue
                helper(nums, i + 1, t - num, track + [num])
        helper(candidates, 0, target, [])
        return res
                