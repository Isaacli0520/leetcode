class Solution:
    # Fast moves forward, for any value that is 
    # not equal to nums[slow], move slow forward
    # and assign it to slow
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1