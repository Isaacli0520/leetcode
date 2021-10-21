class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            print(left, right)
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                return True
            
            # Deals with case 1 1 1 2 1
            while left < mid and nums[left] == nums[mid]:
                left += 1
            while right > mid and nums[right] == nums[mid]:
                right -= 1
            
            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False