class Solution:
    # DP optimized
    # Since every dp[i][j] depends on dp[i - 1][:] and dp[i][:j]
    # we can use a 1d array
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        target = tot // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # goes backward in case an item is used multiple times
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
                
        return dp[-1]
    
    # DP
    # sum(A) = sum(B)
    # sum(A) = sum(nums) // 2
    # dp[i][j] = if the there is a way to pick from
    # the first i elements such that they sum up to j
    # 1. Do not pick nums[i]
    #   dp[i][j] = dp[i - 1][j]
    # 2. Pick nums[i]
    #   dp[i][j] = dp[i - 1][j - nums[i]]
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        target = tot // 2
        dp = [[False] * (target + 1) for i in range(len(nums) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[-1][-1]