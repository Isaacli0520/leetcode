class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prev = 1
        for i in range(1, len(nums)):
            res[i] *= nums[i - 1] * res[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= nums[i + 1] * prev
            prev = prev * nums[i + 1]
        return res