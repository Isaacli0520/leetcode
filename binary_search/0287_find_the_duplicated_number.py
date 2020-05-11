class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        # find meeting point
        while slow != fast:
            slow = nums[slow] # one step
            fast = nums[nums[fast]] # two steps
            
        # find entry point
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow