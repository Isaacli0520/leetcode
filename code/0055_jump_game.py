class Solution:
    # Going forward
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        for i, n in enumerate(nums):
            if i > max_pos:
                return False
            max_pos = max(max_pos, i + nums[i])
        return True
                
    # Going Backward
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        # If we can get to our target from i,
        # our new target is i
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0
        