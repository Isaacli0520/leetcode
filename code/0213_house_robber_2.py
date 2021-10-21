class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(m):
            prev, curr = 0, m[0]
            for i in range(1, len(m)):
                prev, curr = curr, max(prev + m[i], curr)
            return curr
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # Max of [robbing house 1 to n - 1] and [robbing house 2 to n]
        return max(helper(nums[:-1]), helper(nums[1:]))