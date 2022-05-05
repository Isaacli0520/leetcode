class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        res = []
        n = len(nums)
        # Pick left one first, then move middle and right pointer
        for k in range(n - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i, j = k + 1, n - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    j -= 1
                else:
                    i += 1
        return res