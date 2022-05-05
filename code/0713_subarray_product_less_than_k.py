class Solution:
    # For each idx right, find the smallest idx left such that product
    # of nums[left:right + 1] < k, if curr product is too big, we simply
    # divide product by nums[left] and increase left 
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod = 1
        left = 0
        res = 0
        for right in range(len(nums)):
            prod *= nums[right]
            while left <= right and prod >= k:
                prod /= nums[left]
                left += 1
            res += right - left + 1
        return res