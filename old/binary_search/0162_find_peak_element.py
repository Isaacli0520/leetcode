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