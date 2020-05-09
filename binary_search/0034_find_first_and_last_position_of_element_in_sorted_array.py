class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        res = [-1, -1]
        if l == 0: return res
        left, right = 0, l - 1
        while(left <= right):
            mid = int(right + (left - right)/2)
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if left >= l or nums[left] != target:
            res[0] = -1
        else:
            res[0] = left
        
        left, right = 0, l - 1
        while(left <= right):
            mid = int(right + (left - right)/2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if right >= l or nums[right] != target:
            res[1] = -1
        else:
            res[1] = right
        return res