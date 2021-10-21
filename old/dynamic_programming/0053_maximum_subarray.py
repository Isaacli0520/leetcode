class Solution:
    # DP
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            # If previous sum is negative, max sum so far should just be nums[i]
            # Else count previous sums
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)
    
    
    # Divide and Conquer
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(nums, left, right):
            # Base Case
            if left == right:
                return nums[left]
            
            # Left and Right
            mid = left + (right - left) // 2
            l = helper(nums, left, mid)
            r = helper(nums, mid + 1, right)
            
            # Crossing
            # Find maximum from mid to left
            tot = 0
            max_l, max_r = nums[mid], nums[mid + 1]
            for i in range(mid, left - 1, -1):
                tot += nums[i]
                max_l = max(max_l, tot)
            # Find maximum from mid to right
            tot = 0
            for i in range(mid + 1, right + 1):
                tot += nums[i]
                max_r = max(max_r, tot)
            return max(l, r, max_l + max_r)
        
        return helper(nums, 0, len(nums) - 1)