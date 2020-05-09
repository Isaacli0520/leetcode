class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left, right = 0, l - 1
        # Find pivot
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        rot = left
        # Binary Search
        left, right = 0, l - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            idx = (mid + rot) % l
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                left = mid + 1
            elif nums[idx] > target:
                right = mid - 1
        return -1