class Solution:
    # Move slow when current count of nums[fast] is <= 2
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        cnt = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                cnt = 0
            cnt += 1
            if cnt <= 2:
                nums[slow] = nums[fast]
                slow += 1
        return slow