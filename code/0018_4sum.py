class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        # [start, end]
        def helper(start, end, n, target):
            res = []
            if n > 2:
                for i in range(start, end - n + 2):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    for j in helper(i + 1, end, n - 1, target - nums[i]):
                        res.append([nums[i]] + j)
            elif n == 2:
                while start < end:
                    if nums[start] + nums[end] == target:
                        res.append([nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1
                    elif nums[start] + nums[end] > target:
                        end -= 1
                    else:
                        start += 1
            return res
        
        return helper(0, len(nums) - 1, 4, target)