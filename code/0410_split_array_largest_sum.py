class Solution:
    # Decide the minimum max sum that can split array into m subarrays
    #
    # Do a binary search on the max sum and try to minimize it such 
    # that the array can be splitted into m subarrays.
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            cur = 0
            n = 1
            for num in nums:
                if cur + num > mid:
                    n += 1
                    cur = 0
                cur += num
            if n == m:
                right = mid
            elif n < m:
                right = mid
            elif n > m:
                left = mid + 1
        return left