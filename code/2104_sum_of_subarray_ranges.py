class Solution:
    # Naive way
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            mini, maxi = nums[i], nums[i]
            for j in range(i + 1, len(nums)):
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[j])
                res += maxi - mini
                
        return res