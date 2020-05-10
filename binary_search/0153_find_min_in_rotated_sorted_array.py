class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        left, right = 0, l - 1
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        return nums[right]