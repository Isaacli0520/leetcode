class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def count(cp):
            cur = cp
            tot = 1
            for weight in weights:
                if weight <= cur:
                    cur -= weight
                else:
                    cur = cp - weight
                    tot += 1
            return tot
        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            num = count(mid)
            if days == num:
                right = mid
            elif days > num:
                right = mid
            elif days < num:
                left = mid + 1
        return left