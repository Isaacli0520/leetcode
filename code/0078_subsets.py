class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(path, start):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                helper(path, i + 1)
                path.pop()
        helper([], 0)
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(curr, idx):
            if idx == len(nums):
                res.append(curr[:])
                return
            curr.append(nums[idx])
            helper(curr, idx + 1)
            curr.pop()
            helper(curr, idx + 1)
        
        helper([], 0)
        return res