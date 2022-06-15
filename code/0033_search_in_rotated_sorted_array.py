class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        
        # 4 5 6 7 8 9 1 2 3 && 4 < 8 > 3 
        # 7 8 9 1 2 3 4 5 6 && 7 > 2 < 6
        while left < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] > nums[left]:
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[left]:
                    left = mid + 1
                elif target >= nums[left]:
                    right = mid
            elif nums[mid] <= nums[left]:
                if target < nums[mid]:
                    right = mid
                elif target > nums[right - 1]:
                    right = mid
                elif target <= nums[right - 1]:
                    left = mid + 1
        return -1