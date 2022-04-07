class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ceil(a, b):
            return -(a // -b)
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            num = sum([ceil(pile, mid) for pile in piles])
            if h == num:
                right = mid
            elif h < num:
                left = mid + 1
            elif h > num:
                right = mid
        return left