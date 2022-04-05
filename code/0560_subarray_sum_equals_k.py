import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1
        sums = 0
        cnt = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums - k in d:
                cnt += d[sums - k]
            d[sums] += 1
        return cnt