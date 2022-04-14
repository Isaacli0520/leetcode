class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(path, curr_diff, idx):
            if curr_diff == 0:
                res.append(path[:])
                return
            for i in range(idx, len(candidates)):
                num = candidates[i]
                if num <= curr_diff:
                    path.append(num)
                    helper(path, curr_diff - num, i)
                    path.pop()
        
        helper([], target, 0)
        return res