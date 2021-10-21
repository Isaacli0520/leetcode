class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        res = [-1, -1]
        
        # Find Right
        # Key diff from normal binary search:
        #   When nums[mid] == target, shrink left bound
        while left <= right:
            mid = int(left + (right - left) / 2)
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
         # Target is less than every element, right = -1
        if right < 0 or nums[right] != target:
            res[1] = -1
        else:
            res[1] = right
        
        # Find Left
        # Key diff from normal binary search:
        #   When nums[mid] == target, shrink right bound
        left, right = 0, n - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1
            
        # Target is bigger than every element, left = -1
        if left >= n or nums[left] != target:
            res[0] = -1
        else:
            res[0] = left
            
        return res