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