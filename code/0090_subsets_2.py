class Solution:
    # Sort nums first
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        
        def helper(path, start):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                helper(path, i + 1)
                path.pop()
        
        helper([], 0)
        return res

    # Use counter
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        c = Counter(nums)
        cands = list(c.keys())
        
        def helper(path, start):
            res.append(path[:])
            
            for i in range(start, len(cands)):
                cand = cands[i]
                if c[cand]:
                    path.append(cand)
                    c[cand] -= 1
                    helper(path, i)
                    c[cand] += 1
                    path.pop()
        
        helper([], 0)
        return res