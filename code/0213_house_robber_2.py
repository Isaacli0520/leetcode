class Solution:
    # DP
    # run dp twice for nums[:-1], nums[1:] and return max
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(start, end):
            prev, curr = 0, 0
            for i in range(start, end):
                prev2 = prev
                prev = curr
                curr = max(curr, prev2 + nums[i])
            return curr
        
        return max(helper(0, len(nums) - 1), helper(1, len(nums)))