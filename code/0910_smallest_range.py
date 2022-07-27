class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # Bucket Sort
        #
        # maxi, mini = -1, 10001
        # d = defaultdict(int)
        
        # for num in nums:
        #     d[num] += 1
        #     mini = min(mini, num)
        #     maxi = max(maxi, num)
        
        # if maxi - mini <= k:
        #     return maxi - mini
        # if maxi - mini >= 4 * k:
        #     return maxi - mini - 2 * k
        
        # ls = []
        # for i in range(mini, maxi + 1):
        #     if i in d:
        #         ls += [i] * d[i]
        
        ls = sorted(nums)
        res = ls[-1] - ls[0]
        for i in range(len(nums) - 1):
            high = max(ls[-1] - k, ls[i] + k)
            low = min(ls[0] + k, ls[i + 1] - k)
            res = min(res, high - low)
        return res