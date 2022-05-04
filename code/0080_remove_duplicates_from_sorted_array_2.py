class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        slow, fast = 1, 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                cnt = 1
                nums[slow] = nums[fast]
                slow += 1
            elif cnt <= 1:
                cnt += 1
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow