class Solution:
    # DP
    # Assume list A contains positives and B contains nums that are going
    # to be turned into negatives
    # sum(A) - sum(B) = target
    # 2 * sum(A) = target + sum(A) + sum(B)
    # sum(A) = (target + sum(nums)) / 2
    # Therefore, we are trying to find a sublist of nums, which has 
    # a sum of (target + sum(nums)) / 2
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tot = sum(nums)
        if tot < abs(target) or (target + tot) % 2 == 1:
            return 0
        
        # DP
        # dp[i][j] = number of ways to choose from first i items
        #            of array nums such that they sum up tp j
        # State Transition
        # 1. pick nums[i - 1] (the ith item sinze nums is 0-indexed)
        #   there are dp[i - 1][j - nums[i - 1]] ways
        # 1. do not pick nums[i - 1]
        #   there are dp[i - 1][j] ways
        # dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
        def helper(nums, goal):
            # 2d array of size len(nums) * goal
            dp = [[0] * (goal + 1) for _ in range(len(nums) + 1)]
            # Base
            dp[0][0] = 1
            for i in range(1, len(nums) + 1):
                for j in range(goal + 1):
                    if nums[i - 1] <= j:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                    else:
                        dp[i][j] = dp[i - 1][j]
            return dp[-1][-1]
            
        return helper(nums, (target + tot) // 2)
    
        
        
#     def __init__(self):
#         self.d = {}
        
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         if len(nums) == 1:
#             return int(nums[0] == target) + int(nums[0] == -target)
        
#         s = " ".join([str(num) for num in nums]) + "-" + str(target)
#         if s in self.d:
#             return self.d[s]
#         tmp = self.findTargetSumWays(nums[1:], target - nums[0]) + self.findTargetSumWays(nums[1:], target + nums[0])
#         self.d[s] = tmp
#         return tmp
        
                