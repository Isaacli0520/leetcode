class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(candidates)
        
        def helper(path, curr_diff, idx):
            if curr_diff == 0:
                res.append(path[:])
                return
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                if nums[i] <= curr_diff:
                    path.append(nums[i])
                    helper(path, curr_diff - nums[i], i + 1)
                    path.pop()
        
        helper([], target, 0)
        return res