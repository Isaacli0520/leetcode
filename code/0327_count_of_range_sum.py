class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        
        # [lo, hi)
        def sort(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = lo + (hi - lo) // 2
            count = sort(lo, mid) + sort(mid, hi)
            i, j = mid, mid
            for left in presum[lo:mid]:
                # Find lowest num's index i in sorted right
                # s.t. presum[i] - left >= lower
                while i < hi and presum[i] - left < lower:
                    i += 1
                # Find lowest num's index j in sorted right
                # s.t. presum[j] - left > upper (presum[j - 1] - left <= upper)
                while j < hi and presum[j] - left <= upper:
                    j += 1
                count += (j - 1) - i + 1
            # Merge the sorted left and right
            presum[lo:hi] = sorted(presum[lo:hi])
            return count
        return sort(0, len(presum))