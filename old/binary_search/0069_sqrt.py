class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while(left <= right):
            mid = int(left + (right - left)/2)
            if mid == x/mid:
                return mid
            elif mid < x/mid:
                left = mid + 1
            elif mid > x/mid:
                right = mid - 1
        return right