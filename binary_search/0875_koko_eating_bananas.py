class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            s = sum([-(-a // mid) for a in piles])
            if s > H:
                left = mid + 1
            elif s < H:
                right = mid
            else:
                right = mid
        return left