class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while left <= right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                return mid
            # 4 5 6 7 8 0 1  nums[mid] > nums[right]
            #      mid
            if nums[mid] >= nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 5 6 0 1 2 3 4  nums[mid] < nums[right]
            #      mid
            elif nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
                
            
    
#     def search(self, nums: List[int], target: int) -> int:
#         # Find Pivot index first
#         # Modifies mid idx with pivot index to make this a normal binary search
        
#         # Find Pivot
#         n = len(nums)
#         left, right = 0, n - 1
#         while left < right:
#             mid = int(left + (right - left) / 2)
#             if nums[mid] > nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid
#         rot = left
        
#         # Normal binary search
#         left, right = 0, n - 1
#         while left <= right:
#             mid = int(left + (right - left) / 2)
#             idx = (mid + rot) % n
#             if nums[idx] == target:
#                 return idx
#             elif nums[idx] > target:
#                 right = mid - 1
#             elif nums[idx] < target:
#                 left = mid + 1
#         return -1