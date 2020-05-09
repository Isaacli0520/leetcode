class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left, right = 0, l - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            
            if nums[mid] == target:
                return True
            
            # tricky part
            while left < mid and nums[left] == nums[mid]: 
                left += 1
            
            # first half is ordered
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # second half is ordered
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
