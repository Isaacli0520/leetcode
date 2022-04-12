class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int(left + (right - left) / 2)
            # If mid is increasing, there must be a peak on the right
            # Because rightmost is -inf
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # If mid is decreasing, there must be a peak on the left
            # Becasue leftmost is - inf
            else:
                right = mid
        return left

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums)
        i = 0
        while left < right:
            mid = left + (right - left) // 2
            print(mid)
            if (mid == 0 or nums[mid - 1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            
            if mid == 0 or nums[mid - 1] < nums[mid]:
                left = mid + 1
            else:
                right = mid
                
        return left