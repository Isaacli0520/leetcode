class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        left, right = 0, l - 1
        
        # End condition, left == right
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        # Can also return nums[right], cuz left == right in the end
        return nums[left]