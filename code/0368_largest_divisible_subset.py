class Solution:
    # Sort nums first
    # Maintain a dict of set S. S[x] = by far larget subset with x 
    # as the largest element, so x is a multiple of all nums in S[x].
    #
    # For every new num, we divide it with all keys in S and add a new
    # key with value being the divisible set with most nums.
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        sets = {}
        for num in sorted(nums):
            ls = [sets[s] for s in sets if num % s == 0]
            if len(ls) == 0:
                sets[num] = set([num])
            else:
                tmp = max(ls, key=len)
                sets[num] = tmp | {num}
        return list(max(sets.values(), key=len))