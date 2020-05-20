class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     self.dp = {}
    #     def helper(m, start):
    #         if start >= len(m):
    #             return 0
    #         if start in self.dp:
    #             return self.dp[start]
    #         self.dp[start] = max(m[start] + helper(m, start + 2), helper(m, start + 1))
    #         return self.dp[start]
    #     return helper(nums, 0)
    
    # O(1) space
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev, curr = 0, nums[0]
        # curr - dp[i - 1]
        # prev - dp[i - 2]
        # dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        for i in range(1, len(nums)):
            prev, curr = curr, max(prev + nums[i], curr)
        return curr