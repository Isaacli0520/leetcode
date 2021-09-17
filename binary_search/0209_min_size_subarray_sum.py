class Solution:
    # def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    #     result = len(nums) + 1
    #     left = 0
    #     for i, n in enumerate(nums[1:], 1):
    #         nums[i] = nums[i - 1] + n
    #     for right, n in enumerate(nums):
    #         if n >= s:
    #             target = n - s
    #             l, r = left, right
    #             while l < r:
    #                 mid = l + (r - l) // 2
    #                 if nums[mid] <= target:
    #                     l = mid + 1
    #                 elif nums[mid] > target:
    #                     r = mid
    #             left = l
    #             result = min(result, right - left + 1)
    #     return result if result != len(nums) + 1 else 0
        
    
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        tot = 0
        result = n + 1
        left = 0
        # Move right pointer, find minimal length of contiguous subarr
        # with every right pointer
        for right, y in enumerate(nums):
            tot += y
            # Current tot is too big, move left pointer
            while target <= tot:
                result = min(result, right - left + 1)
                tot -= nums[left]
                left += 1
        return result if result != n + 1 else 0
        