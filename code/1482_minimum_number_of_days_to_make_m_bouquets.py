class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            cur = 0
            tot = 0
            for day in bloomDay:
                if day <= mid:
                    cur += 1
                    if cur >= k:
                        tot += 1
                        if tot == m:
                            break
                        cur = 0
                else:
                    cur = 0
            if tot >= m:
                right = mid
            elif tot < m:
                left = mid + 1
        return left