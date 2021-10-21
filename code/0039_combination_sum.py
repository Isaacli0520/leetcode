class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(nums, t, track):
            if t == 0:
                res.append([i for i in track])
                return
            for i, num in enumerate(nums):
                if t >= num:
                    track.append(num)
                    helper(nums[i:], t - num, track)
                    track.pop()
                    
        helper(candidates, target, [])
        return res