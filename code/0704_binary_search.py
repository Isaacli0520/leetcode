class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            num = nums[mid]
            if target == num:
                return mid
            elif target < num:
                right = mid
            elif target > num:
                left = mid + 1
        return -1