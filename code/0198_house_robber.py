class Solution:
    # DP optimized
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for num in nums:
            prev2 = prev
            prev = curr
            curr = max(prev, prev2 + num)
        return curr
        
    # DP
    # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = nums[:]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]