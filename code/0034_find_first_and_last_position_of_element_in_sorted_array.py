class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Left Bound
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            num = nums[mid]
            # Shrink Left
            if target == num:
                right = mid
            elif target < num:
                right = mid
            elif target > num:
                left = mid + 1
        lb = left if left != len(nums) and nums[left] == target else -1
        
        # Right Bound
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            num = nums[mid]
            # Shrink Right
            if target == num:
                left = mid + 1
            elif target < num:
                right = mid
            elif target > num:
                left = mid + 1
        rb = left - 1 if left > 0 and nums[left - 1] == target else -1
        
        return [lb, rb]