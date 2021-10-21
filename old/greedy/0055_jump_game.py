class Solution:
    # Going forward
    def canJump(self, nums: List[int]) -> bool:
        # Maximum distance we can go
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True
    
    # Going backwards
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            # If we can get to goal from i,
            # out new goal is set to i
            if i + nums[i] >= goal:
                goal = i
        return goal == 0