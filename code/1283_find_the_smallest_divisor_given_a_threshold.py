class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def ceil(a, b):
            return -(a // -b)
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            num = sum([ceil(n, mid) for n in nums])
            if num == threshold:
                right = mid
            elif num < threshold:
                right = mid
            elif num > threshold:
                left = mid + 1
        return left